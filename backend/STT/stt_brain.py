# ============================================================
# Importados
# ============================================================

from faster_whisper import WhisperModel
from pathlib import Path
import time

# ============================================================
# Configuracion de stt_brain
# ============================================================

basedir = Path(__file__).parent.parent
localdir = basedir / "STT"
audio_folder_path = localdir / "recordings"
audio_file = audio_folder_path / "audio.wav"
localdir = basedir / "STT"
# IMPORTANTE: llm_queue apunta a LLM/llm_queue.txt, no a TTS/tts_queue.txt que soy imbécil y no se escribir rutas.
llm_queue = basedir / "LLM" / "llm_queue.txt"

if llm_queue.exists():
    print("Encontrado: llm_queue")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="float32"
)

# ============================================================
# Función transmitir a LLM
# ============================================================

def transmitir():
    with open(llm_queue, "a", encoding="utf-8") as file:
                    file.write(final_user_input)


# ============================================================
# Loop principal
# ============================================================

while True:

    if audio_file.exists():
        complete_user_input = ""
        segments, info = model.transcribe(
            audio_file,
            language="es"
        )
        for segment in segments:
            print(segment.text)
            complete_user_input += segment.text
        final_user_input = complete_user_input
        transmitir()
        audio_file.unlink()
    else:
        print("No hay audio que transcribir")
        time.sleep(0.5)



