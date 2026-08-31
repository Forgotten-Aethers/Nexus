import sys
import subprocess
from pathlib import Path
import atexit

basedir = Path(__file__).parent
llm_queue = basedir / "LLM" / "llm_queue.txt"
tts_queue = basedir / "TTS" / "tts_queue.txt"
llm_brain = basedir / "LLM" / "llm_brain.py"
stt_brain = basedir / "STT" / "stt_brain.py"
recorder = basedir / "STT" / "recorder.py"
tts_brain = basedir / "TTS" / "tts_brain.py"

def cleaning_at_exit():
        for proceso in procesos:
                proceso.terminate()
        for proceso in procesos:
                proceso.wait()

atexit.register(cleaning_at_exit)

if llm_queue.exists() and tts_queue.exists():
    print("Encontrados: llm_queue y tts_queue")

with open(llm_queue, "w", encoding="utf-8") as file:
                    file.write("")
with open(tts_queue, "w", encoding="utf-8") as file:
                    file.write("")

procesos = []

procesos.append(subprocess.Popen([sys.executable, llm_brain], creationflags=subprocess.CREATE_NEW_CONSOLE))
procesos.append(subprocess.Popen([sys.executable, tts_brain], creationflags=subprocess.CREATE_NO_WINDOW))
procesos.append(subprocess.Popen([sys.executable, stt_brain], creationflags=subprocess.CREATE_NO_WINDOW))
procesos.append(subprocess.Popen([sys.executable, recorder], creationflags=subprocess.CREATE_NO_WINDOW))

input("Pulse enter para cerrar el programa")

