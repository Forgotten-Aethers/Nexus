
# ============================================================
# IMPORTS
# ============================================================

import sys
import os
import atexit
import signal
import subprocess
import json
import datetime
import time
from pathlib import Path

# ============================================================
# Configuración de main.py
# ============================================================

basedir = Path(__file__).parent
sigkill_database = basedir / "data" / "SIGKILL_register"
app = basedir / "frontend" / "app_launcher.py"
if os.name != "nt":
    procs = Path("/proc")

# Si la base de datos no existe, se crea con una lista vacía.
# Esto permite registrar los primeros cierres forzados sin errores.
if not sigkill_database.exists():
    sigkill_database.parent.mkdir(parents=True, exist_ok=True)
    with open(sigkill_database, "w", encoding="utf-8") as file:
        json.dump([], file)

cleaning = False
processes = []
launchers = [app]
encendido = True

# ============================================================
# Registrar cierres forzados
# ============================================================

def sigkill_register(process):
    global sigkill_database_data

    # Se abre la base de datos y se carga su contenido JSON.
    with open(sigkill_database, "r", encoding="utf-8") as file:
        sigkill_database_data = json.load(file)

    # Se crea un registro con el PID del proceso y la fecha del cierre forzado.
    new_sigkill = {
        "process": process.pid,
        "date": datetime.datetime.now().isoformat()
    }

    # Se añade el nuevo registro a la base de datos.
    sigkill_database_data.append(new_sigkill)

    # Se sobrescribe el archivo con los datos actualizados.
    with open(sigkill_database, "w", encoding="utf-8") as file:
        json.dump(sigkill_database_data, file, indent=4)

# ============================================================
# Arranque
# ============================================================

for launcher in launchers:
    # Por cada launcher dentro de la lista launchers.
    if os.name == "nt":
        # WINDOWS:
        # Se inicia el launcher dentro de un nuevo grupo de procesos.
        processes.append(
            subprocess.Popen(
                [sys.executable, str(launcher)],
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
            )
        )
    else:
        # LINUX Y OTROS SISTEMAS POSIX:
        # Se inicia el launcher en una sesión y grupo de procesos nuevos.
        # Esto permite gestionar posteriormente el grupo completo mediante su PGID.
        processes.append(
            subprocess.Popen(
                [sys.executable, str(launcher)],
                start_new_session=True
            )
        )

# ============================================================
# Apagado
# ============================================================

def active_children(pgid):
    active_processes = 0
    for proc in procs.iterdir():
        if not proc.name.isdigit():
            continue
        try:
            with open(proc / "stat", "r") as file:
                data = file.read()
                end = data.rfind(")")
                fields = data[end + 2:].split()

                if int(fields[2]) == pgid:
                    if fields[0] != "Z":
                        active_processes = active_processes + 1
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            continue
    if active_processes == 0:
        return False
    else:
        return True




def kill_children():
    for process in processes:
        # Por cada proceso dentro de la lista processes.

        if os.name == "nt":
            # WINDOWS:
            # Se envía CTRL_BREAK_EVENT al grupo de procesos para solicitar
            # un cierre controlado. Después se espera un máximo de 3 segundos.
            try:
                process.send_signal(signal.CTRL_BREAK_EVENT)
                process.wait(timeout=3)

            except subprocess.TimeoutExpired:
                # Si el proceso no termina dentro del tiempo establecido,
                # se fuerza el cierre de todo su árbol de procesos mediante taskkill.
                subprocess.run(
                    ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                    check=False,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )

                # Se registra el cierre forzado en la base de datos.
                sigkill_register(process)

                # Se espera a que el proceso principal termine definitivamente.
                process.wait()

        else:
            # LINUX:
            # Se obtiene el identificador del grupo al que pertenece el proceso.
            # Al haberse iniciado con start_new_session=True, inicialmente
            # el PID del launcher también es el PGID de su grupo.
            try:
                pgid = os.getpgid(process.pid)

                # SIGTERM solicita el cierre de todos los procesos del grupo.
                os.killpg(pgid, signal.SIGTERM)

                # Se comprueba durante un máximo de 3 segundos si el grupo
                # continúa existiendo. 300 iteraciones x 0,01 segundos = 3 segundos.
                for i in range(300):
                    try:
                        # La señal 0 no termina procesos: únicamente comprueba
                        # si el grupo existe y si se tiene permiso para acceder a él.
                        if active_children(pgid) == False:
                            break
                        time.sleep(0.01)

                    except ProcessLookupError:
                        # Si el grupo ya no existe, todos sus procesos han desaparecido.
                        break

                else:
                    # El else se ejecuta si el bucle termina sin encontrar un break.
                    # Es decir, si el grupo sigue existiendo después de los 3 segundos.

                    # SIGKILL fuerza la terminación de todos los procesos del grupo.
                    os.killpg(pgid, signal.SIGKILL)

                    # Se registra que ha sido necesario forzar el cierre.
                    sigkill_register(process)

                    # Se recoge el estado de terminación del proceso principal.
                process.wait()
            except ProcessLookupError:
                # El proceso o su grupo han desaparecido antes de poder actuar.
                # No es necesario hacer nada más.
                pass

# ============================================================
# Protección ante doble cierre
# ============================================================

def cleanup():
    global cleaning
    global encendido

    # Evita que el procedimiento de apagado se ejecute varias veces
    # simultáneamente o de forma recursiva.
    if cleaning:
        return

    # Se marca el inicio del apagado antes de comenzar a cerrar procesos.
    cleaning = True

    try:
        kill_children()
        encendido = False
    except Exception as e:
        # Captura errores inesperados durante el procedimiento de apagado.
        print(f"Error durante el apagado: {e}")

# ============================================================
# Tipos de solicitudes de apagado
# ============================================================

def signal_register(signum, frame):
    # Se ejecuta cuando el sistema operativo envía una señal de cierre.
    # Primero se realiza el apagado controlado y después se termina main.py.
    cleanup()
    sys.exit(0)

# ============================================================
# Detección y ejecución del apagado
# ============================================================

if os.name == "nt":
    # WINDOWS:
    # SIGTERM: solicitud de terminación.
    # SIGINT: interrupción (por ejemplo, Ctrl+C).
    # SIGBREAK: interrupción mediante Ctrl+Break.
    atexit.register(cleanup)
    signal.signal(signal.SIGTERM, signal_register)
    signal.signal(signal.SIGINT, signal_register)
    signal.signal(signal.SIGBREAK, signal_register)

else:
    # LINUX Y OTROS SISTEMAS POSIX:
    # SIGTERM: solicitud de terminación.
    # SIGINT: interrupción (por ejemplo, Ctrl+C).
    atexit.register(cleanup)
    signal.signal(signal.SIGTERM, signal_register)
    signal.signal(signal.SIGINT, signal_register)

while encendido == True:
    time.sleep(0.1)
# Nota:
# En Windows cada sublauncher tendrá que esperar a que sus subprocesos
# cierren, para evitar sobrecargar main.py con detecciones de grupo
# y agrupaciones manuales.
