# ============================================================
# IMPORTS
# ============================================================

import ollama
from pathlib import Path
import json
from datetime import datetime
import time

# ============================================================
# Configuración del LLM
# ============================================================

model = "gemma4:12b"
basedir = Path(__file__).parent.parent
localdir = basedir / "LLM"
datadir = localdir / "data"
sysprompt_path = datadir / "systemprompt.txt"
conversations_path = datadir / "conversations.json"
with open(conversations_path, "r", encoding="utf-8") as file:
    conversations = json.load(file)
conversation_folder = datadir / "conversations"
tts_queue = basedir / "TTS" / "tts_queue.txt"
llm_queue = localdir / "llm_queue.txt"

# ============================================================
# System prompt
# ============================================================

print("-----------------------------------------------------------------------------", end="\n\n")
print("Buscando:", sysprompt_path)
print("¿Existe?:", sysprompt_path.exists(), end="\n\n")
print("-----------------------------------------------------------------------------", end="\n\n")

def get_sysprompt():
    with open(sysprompt_path, "r", encoding="utf-8") as sysprompt:
        return sysprompt.read()

system_prompt = get_sysprompt()

# ============================================================
# Construyendo el historial de la conversación
# ============================================================

history = []

conversation_id = input("Presiona Enter para iniciar una conversación con Nexus o escribe el id de conversación para cargarlo: ")
for conversation in conversations:
    if conversation["id"] == conversation_id:
        conversation_path = conversation_folder / f"{conversation_id}.json"
        with open(conversation_path, "r", encoding="utf-8") as file:
            history = json.load(file)
        break
else:
        print("No se encontró la conversación. Iniciando una nueva conversación.")
        conversation_id = datetime.now().strftime("%Y%m%d%H%M%S")
        conversation_path = conversation_folder / f"{conversation_id}.json"
        conversations.append({"id": conversation_id, "path": str(conversation_path)})
        with open(conversations_path, "w", encoding="utf-8") as file:
            json.dump(conversations, file, ensure_ascii=False, indent=4)
        history.append({
            "role": "system",
            "content": system_prompt
        })
        with open(conversation_path, "w", encoding="utf-8") as file:
            json.dump(history, file, ensure_ascii=False, indent=4)

# ============================================================
# Funciones para guardar la conversación
# ============================================================

def save_conversation():
    with open(conversation_path, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

def save_user(user_input):
    history.append({
        "role": "user",
        "content": user_input
    })

def save_assistant(thinking, response):
    history.append({
        "role": "assistant",
        "thinking": thinking,
        "content": response
    })

# ============================================================
# Input de usuario
# ============================================================

def get_user_input():

    while True:

        if llm_queue.exists():

            user_input = llm_queue.read_text(encoding="utf-8").strip()

            if user_input != "":
                llm_queue.write_text("", encoding="utf-8")
                print("Input: ", user_input)
                return user_input

        time.sleep(0.1)

# ============================================================
# Generar respuesta de Nexus
# ============================================================

def generate_response():

    # Informar al usuario que se está construyendo el modelo de IA
    print("\nBuilding up the AI model...\n")

    # Generar la respuesta de Nexus
    stream = ollama.chat(
        model= model,
        messages= history,
        stream= True,
        think= True
    )

    thinking = ""
    response = ""

    # Trabajamos cada chunk de la respuesta de Nexus
    for chunk in stream:

        # Si el chunk contiene un mensaje de pensamiento, lo mostramos en la terminal
        if chunk.message.thinking:
            # Si es el primer chunk de pensamiento, imprimimos un encabezado
            if thinking == "":
                print("\n\nNexus' reasoning:")
            # Vamos construyendo el mensaje de pensamiento y lo mostramos en la terminal
            print(chunk.message.thinking, end="", flush=True)
            thinking += chunk.message.thinking

        # Si el chunk contiene un mensaje de contenido, lo mostramos en la terminal
        if chunk.message.content:
            # Si es el primer chunk de contenido, imprimimos un encabezado
            if response == "":
                print("\n\nNexus:")
            # Vamos construyendo el mensaje de contenido y lo mostramos en la terminal
            print(chunk.message.content, end="", flush=True)
            response += chunk.message.content

            # Guardamos el chunk de contenido en la cola de TTS
            with open(tts_queue, "a", encoding="utf-8") as file:
                file.write(chunk.message.content)

    # Guardamos un salto de línea al final de la cola de TTS para separar las respuestas
    with open(tts_queue, "a", encoding="utf-8") as file:
        file.write("\n")
    print("\n")

    return thinking, response

# ============================================================
# Informando al usuario
# ============================================================

print(f"--- Nexus conectado a {model} ---")
print("Bienvenido a la terminal de Nexus\n")
print("Escribe 'salir' para terminar la sesión.\n")

# ============================================================
# Loop principal
# ============================================================

while True:

    # Preguntamos al usuario por su input
    user_input = get_user_input()

    # Si el usuario quiere salir, rompemos el bucle
    if user_input is None:
        break

    # Guardamos el input del usuario en la conversación
    save_user(user_input)

    # Generamos la respuesta de Nexus
    thinking, response = generate_response()

    # Guardamos la respuesta de Nexus
    save_assistant(thinking, response)
    # Guardamos la conversación en el archivo correspondiente
    save_conversation()