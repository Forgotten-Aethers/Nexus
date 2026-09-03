# ============================================================
# Importados
# ============================================================

import sounddevice as sd
from scipy.io.wavfile import write
import keyboard
import time
from pathlib import Path

# ============================================================
# Configuracion de recorder
# ============================================================

basedir = Path(__file__).parent.parent
localdir = basedir / "STT"
audio_folder_path = localdir / "recordings"
ubicacion_audio = audio_folder_path / "audio.wav"

if not audio_folder_path.exists():
    audio_folder_path.mkdir(parents=True, exist_ok=True)

frecuency = 16000
grabando = False
audio = None
inicio = 0

# ============================================================
# Función de grabar
# ============================================================

def recordaudio():

    global grabando, audio, inicio

    if not grabando:
        #Informando al usuario
        print("Comenzando grabación")
        #Cambiando variable
        grabando = True
        #Empezar grabación
        audio = sd.rec(
                    int(frecuency * 180),
                    samplerate=frecuency,
                    channels=1,
                    dtype="int16",
                )
        inicio = time.time()
    else:
        #Informando al usuario
        print("Cerrando grabación")
        #Cambiando variable
        grabando = False
        #Cerrar grabación
        sd.stop()
        #Estableciendo duración
        fin = time.time()
        segundos = fin - inicio
        muestras_grabadas = int(frecuency * segundos)
        audio = audio[:muestras_grabadas]
        print("Duración: ", segundos)
        #Escribiendo archivo
        write(ubicacion_audio, frecuency, audio)
        print("Audio creado en Nexus 1.0/SST/recordings")

# ============================================================
# Creando hotkey
# ============================================================

keyboard.add_hotkey("ctrl+m", recordaudio, suppress=True)

# ============================================================
# Informando al ususario
# ============================================================

print("Pulsa Ctrl+M para empezar.")

# ============================================================
# Loop principal
# ============================================================

keyboard.wait()


