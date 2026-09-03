# ============================================================
# Librerías
# ============================================================

from pathlib import Path
import time
import piper
import sounddevice as sd
from piper.config import SynthesisConfig

# ============================================================
# Configuración del TTS
# ============================================================

basedir = Path(__file__).parent.parent
localdir = basedir / "TTS"
queue_path = localdir / "tts_queue.txt"
voice_path = localdir / "voices" / "es_ES-sharvard-medium.onnx"
voice = piper.PiperVoice.load(voice_path)

stream = sd.OutputStream(
    samplerate=voice.config.sample_rate,
    channels=1,
    dtype="float32"
)

stream.start()

# ============================================================
# Preparar la cola de TTS
# ============================================================

def prepare_queue():

    # Leer siempre el contenido actual de la cola
    with open(queue_path, "r", encoding="utf-8") as file:
            queue_content = (
                  file.read()
                  .replace("\n", " ")
                  .replace ("*", "")
                  .replace ("#", ""))
    return queue_content

# ============================================================
# Filtrar la cola de TTS
# ============================================================

def find_sentence_end(queue_content):
    valores = [
        queue_content.find("."),
        queue_content.find("?"),
        queue_content.find("!")
    ]

    print("Primer punto:", valores[0])
    print("Primer signo de interrogación:", valores[1])
    print("Primer signo de exclamación:", valores[2])

    valores_filtrados = [x for x in valores if x != -1]
    return valores_filtrados

# ==============================================================================================================================
# Conseguir el fragmento de texto hasta el primer punto, signo de interrogación o signo de exclamación.
# ==============================================================================================================================

def get_fragment(queue_content, valores_filtrados):

    valor_minimo = min(valores_filtrados)

    print("Valor mínimo:", valor_minimo)

    fragmento = queue_content[:valor_minimo + 1]
    resto = queue_content[valor_minimo + 1:]

    print("Fragmento:", fragmento)

    # Actualizar la cola
    with open(queue_path, "w", encoding="utf-8") as file:
        file.write(resto)

    return fragmento

# ============================================================
# Reproducir el fragmento de texto
# ============================================================

def play_fragment(fragmento):

    syn_config = SynthesisConfig(
        speaker_id=1,
        length_scale=0.85,
        noise_scale=0.8,
        noise_w_scale=0.5,
        volume=1.0
    )

    contador = 0

    for audio_chunk in voice.synthesize(fragmento, syn_config):

        contador += 1

        print(
            f"Chunk {contador} - "
            f"{len(audio_chunk.audio_float_array)} muestras"
        )

        stream.write(audio_chunk.audio_float_array)
    time.sleep(0.25)

    print(f"Fragmento terminado ({contador} chunks)")
    
# ============================================================
# Bucle principal
# ============================================================

while True:

    # Preparar la cola de TTS

    queue_content = prepare_queue()

    # Si la cola está vacía, esperamos un poco antes de volver a comprobar

    if queue_content == "":
        print("La cola de TTS está vacía.")
        time.sleep(0.05)
        continue

    # Si la cola tiene contenido, procesamos el primer fragmento de texto hasta el primer punto, signo de interrogación o signo de exclamación

    valores_filtrados = find_sentence_end(queue_content)

    # Si aún no hay una frase completa esperamos

    if not valores_filtrados:
        print("Esperando a que termine la frase...")
        time.sleep(0.05)
        continue

    # Si hay una frase completa, obtenemos el fragmento de texto hasta el primer punto, signo de interrogación o signo de exclamación

    fragmento = get_fragment(queue_content, valores_filtrados)
    
    ## Sintetizar el fragmento de texto y reproducirlo

    play_fragment(fragmento)


    



