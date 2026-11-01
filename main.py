# ============================================================
# IMPORTS
# ============================================================

import sys
import os
import atexit
import signal
import subprocess
from pathlib import Path

# ============================================================
# Configuración de main.py
# ============================================================

basedir = Path(__file__).parent
app = basedir / "frontend" / "app_launcher.py"

processes = []

launchers = [app]

# ============================================================
# Arranque
# ============================================================

for launcher in launchers:
    # Por cada "launcher" dentro de la lista "launchers"
    if os.name == "nt":
        # Si el sistema es windows, ejecuta el launcher dentro de su propio grupo de procesos
        processes.append(subprocess.Popen([sys.executable, str(launcher)], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP))
    else:
        # Si el sistema es otro, ejecuta el launcher dentro de su propio grupo de procesos
        processes.append(subprocess.Popen([sys.executable, str(launcher)], start_new_session=True))

# ============================================================
# Apagado
# ============================================================

def kill_children():
    for process in processes:
        # Por cada "process" dentro de la lista "processes"
        if process.poll() is not None:
            # Si el proceso envía su información del cierre, se continua porque ya ha cerrado.
            continue

        if os.name == "nt":
            # Si el sistema es windows, se intenta cerrar controladamente el grupo, si no cierra en un tiempo, se fuerza. Nota: PID es el identificador del proceso, el resto es información sobre como hacerlo.
            try:
                process.send_signal(signal.CTRL_BREAK_EVENT)
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                subprocess.run(
                    ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                    check=False,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                process.wait()
        else:
            # Si el sistema es otro, se intenta cerrar controladamente el grupo, si no cierra en un tiempo, se fuerza.
            try:
                 os.killpg(process.pid, signal.SIGTERM)
                 process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()

# ============================================================
# Detección y ejecución del apagado
# ============================================================

atexit.register(kill_children)