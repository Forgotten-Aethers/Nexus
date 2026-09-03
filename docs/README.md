# Nexus

README.md written in both **English (EN)** and **Spanish (ES)**. If you wish to read in English, **please scroll down until you see "English (EN)" written.**

---

## Español (ES)

### 1. Introducción

Bienvenido a *Nexus*, mi asistente personal.

*Nexus* nació como una idea mientras probaba **Ollama**: ¿Y si creo mi propio asistente personal? Un asistente como los de las películas, que pueda facilitarme la vida. La idea nació con el pensamiento de poder abrir mi ordenador y poder decir:

> *"Nexus, quiero que abras Discord y prepares Minecraft junto al navegador."*

Por alguna extraña razón, pensé que sería divertido crearlo desde cero haciendo uso de **Python** y distintos programas como **Ollama** o **Piper**, por lo que me puse manos a la obra. Ya tenía algo de experiencia programando, pero nada muy grande o notorio; sería mi primer proyecto serio. Decidí emplearlo como una herramienta para aprender y como reto personal.

Ahora bien, ¿por qué subo esto? La pregunta cobra especial importancia teniendo en cuenta que he tenido que aprender a usar *GitHub* y *Git* solo por subirlo. Hay dos razones principales:

1. Aprender a usar estas herramientas me podía ser útil en un futuro y durante el mismo desarrollo de *Nexus*.
2. No lo sé, pensé que estaría bien subirlo y que otras personas pudiesen usarlo y basarse en él si lograban hacerlo funcionar en su ordenador. No tengo ninguna intención de vender la versión actual.

Ahora que ya he explicado cómo lo creé, ¿qué demonios es *Nexus*?

### 2. Descripción

*Nexus* es un asistente de IA personalizado con fines educativos y personales.

Por ende (Nota: **¡qué nivel de lenguaje, Marivel!**), aunque mi propio Roadmap confirma que tengo planeadas actualizaciones de compatibilidad y portabilidad para facilitar descargarlo y usarlo (he pensado en vosotros jajaja), mi prioridad es que funcione para mí, no distribuirlo por todo el mundo ni venderlo.

Si en el futuro el proyecto llega a convertirse en algo lo suficientemente sólido, quizás me plantee otras formas de financiación o incluso comercializarlo. Tendré que comer de algo en el futuro, ¿no?

La idea es que *Nexus* se convierta en un asistente local que haga uso de modelos **STT**, **TTS** y **LLM** para tener entrada y salida de audio, además de respuestas inteligentes y capacidad de **raciocinio**.

Además de todo esto, me gustaría que tuviese acceso a **Internet** y herramientas para que pueda ayudar a programar, abrir aplicaciones, cambiar el volumen, etc.

El objetivo es acabar con una aplicación sólida, con su interfaz, funcionalidades, etc.

No obstante, al momento de escribir esto estoy terminando la **1.0**, primera versión que voy a subir y que solo se centra en que funcione, aunque no use los mejores métodos.

### 3. Estructura

Actualmente (**v1.0**), *Nexus* se compone de tres módulos principales:

- **LLM**
- **TTS**
- **STT**

Estos módulos están compuestos por un archivo `.py` principal (`xxx_brain.py`) que se encarga de orquestar todo el software utilizado.

Por ejemplo, `llm_brain.py` se encarga de transmitir una entrada de texto a nuestro modelo local de **Ollama** (actualmente **Gemma3:12b**), guardar un historial de conversaciones y transmitir la respuesta al módulo TTS.

Si exploras los archivos, también puedes encontrar archivos `.py` secundarios con la tarea de complementar y ayudar a los cerebros del programa.

Además, también puedes encontrar archivos `.txt` intermediarios. Es decir, son utilizados por los módulos para comunicarse entre ellos.

Lo más probable es que desaparezcan si sigo con mi plan de desarrollo, ya que uno de los objetivos es que los módulos se comuniquen a través de la **RAM**.

### 4. Características actuales

La versión **1.0** de *Nexus* se centra en poner en funcionamiento el loop principal; es decir, que puedas hablarle a través del micrófono (actualmente predeterminado para español) y que el modelo te responda por los altavoces.

Es decir, no tiene acceso a Internet, utiliza métodos que quizás no son los más prácticos, no tiene acceso a herramientas y quizás no es muy eficiente.

Lo importante es que es la primera versión funcional de *Nexus*.

**Nexus 1.0 tiene como único objetivo que el loop principal tenga lugar.**

*Nexus* sigue en desarrollo.

### 5. Requisitos e instalación

Como he dicho antes, actualmente *Nexus* está pensado para funcionar en mi Python dentro de mi ordenador, aunque considero perfectamente posible descargarlo en cualquier otro dispositivo si trasteamos un poco con él.

Mis componentes son:

- **CPU:** Intel Core i5-13400F
- **GPU:** AMD Radeon 9060 XT
- **Sistema operativo:** Windows 11

Actualmente está testeado y probado en **Windows 11**.

En un futuro planeo intentar hacerlo totalmente portable y facilitar su instalación, pero por el momento depende totalmente de ti.

Puedes encontrar todas las librerías necesarias en `requirements.txt`, situado en la carpeta `docs`, dentro de la raíz del proyecto.

Actualmente, por problemas de compatibilidad con AMD, los módulos **TTS** y **STT** hacen uso de la CPU, ya que son ligeros y hay un cambio muy grande entre utilizarlos en la CPU o GPU. Así que no deberíais tener problemas con la GPU.

### 6. Uso de IA

Vale, antes de que venga alguien a llamarme *vibe coder*, me gustaría aclarar el uso que he hecho de la IA y que el proyecto tiene carácter educativo.

**Todo el código del proyecto está escrito a mano** (o a teclado).

He hecho uso de IAs como **ChatGPT** para que actúen como mi profesor. Me han enseñado y ayudado a usar las librerías, solucionar problemas de compatibilidad, debuggear, desbloquearme cuando me quedaba atascado sin saber cómo seguir, establecer una ruta de proyecto, etc.

Han actuado como profesor y, de hecho, lo han hecho bastante bien. Junto a los tutoriales de YouTube y la documentación online, me han ayudado a entender muchos conceptos.

Toda la arquitectura y el código que hay en *Nexus* han sido escritos a mano y han salido de mí.

### 7. Feedback

Estoy totalmente abierto a **feedback, ideas y críticas constructivas**, siempre que mantengan un tono respetuoso.

No obstante, no acepto presión alguna para actualizar o realizar cambios en *Nexus*. Es software que podéis descargar y utilizar gratuitamente y, más importante aún, un proyecto personal de aprendizaje.

Así que no veo necesidad de tener a alguien presionándome para que lo actualice o cambie alguna arquitectura, etc. Si lo haces repetidamente, probablemente seas ignorado o incluso vetado.

Ahora, como he dicho al principio, si alguien quiere aportar feedback, ideas para mejorar la arquitectura (busco que sea lo más modular posible), hacer más eficiente el código, señalar algún problema de seguridad que pueda haber, etc., estoy totalmente abierto y lo agradecería enormemente.

Lo único que pido es que no me presionen.


## English (EN)

### 1. Introduction

Welcome to *Nexus*, my personal assistant.

*Nexus* was born as an idea while testing **Ollama**: What if I created my own personal assistant? An assistant like the ones in the movies, one that could make my life easier. The idea came from imagining being able to open my computer and say:

> *"Nexus, I want you to open Discord and prepare Minecraft next to the browser."*

For some strange reason, I thought it would be fun to create it from scratch using **Python** and various programs like **Ollama** or **Piper**, so I got to work. I already had some programming experience, but nothing very extensive or noteworthy; it would be my first serious project. I decided to use it as a learning tool and as a personal challenge.

Now, why am I uploading this? The question takes on special importance considering that I had to learn to use *GitHub* and *Git* just to upload it. There are two main reasons:

1. Learning to use these tools could be useful to me in the future and during the development of *Nexus* itself.

2. I don't know, I thought it would be good to upload it so other people could use it and build upon it if they managed to get it working on their computers. I have no intention of selling the current version.

Now that I've explained how I created it, what the heck is *Nexus*?

### 2. Description

*Nexus* is a custom AI assistant for educational and personal purposes.

Therefore (Note: **How Posh!** (Wait, a parenthesis inside a parenthesis? Never mind, this is actually the version I found of a Spanish saying, please look for it in the Spanish section).), although my own Roadmap confirms that I have planned compatibility and portability updates to make it easier to download and use (I was thinking of you all, haha), my priority is that it works for me, not distributing it worldwide or selling it.

If the project becomes something solid enough in the future, I might consider other forms of funding or even commercializing it. I'll have to make a living somehow in the future, right?

The idea is for *Nexus* to become a local assistant that uses **STT**, **TTS**, and **LLM** models for audio input and output, as well as intelligent responses and reasoning capabilities.

In addition to all this, I'd like it to have **Internet** access and tools so it can help with programming, opening applications, changing the volume, etc.

The goal is to eventually have a solid application with its own interface, features, and so on.

However, as I write this, I'm finishing **1.0**, the first version I'm going to upload, which is only focused on making it work, even if it doesn't use the best methods.

### 3. Structure

Currently (v1.0), Nexus consists of three main modules:

- LLM
- TTS
- STT

These modules are composed of a main `.py` file (`xxx_brain.py`) that orchestrates all the software used.

For example, `llm_brain.py` is responsible for transmitting text input to our local `Ollama` model (currently Gemma3:12b), saving a conversation history, and transmitting the response to the TTS module.

If you explore the files, you can also find secondary `.py` files that complement and assist the program's core components.

In addition, you can also find intermediary `.txt` files. These are used by the modules to communicate with each other.

They will most likely disappear if I continue with my development plan, since one of the goals is for the modules to communicate through RAM.

### 4. Current Features

Version 1.0 of Nexus focuses on getting the main loop working; that is, you can speak to it through the microphone (currently set to Spanish by default) and the model will respond through the speakers.

In other words, it doesn't have internet access, uses methods that may not be the most practical, doesn't have access to tools, and is perhaps not very efficient.

The important thing is that it is the first functional version of Nexus.

The sole objective of Nexus 1.0 is to get the main loop working.

Nexus is still under development.

### 5. Requirements and Installation

As I mentioned before, Nexus is currently designed to run on my computer and my current Python environment, although I believe it's perfectly possible to run it on another device with a little tweaking.

My components are:

- **CPU:** Intel Core i5-13400F
- **GPU:** AMD Radeon 9060 XT
- **Operating System:** Windows 11

It has currently been tested on **Windows 11**.

In the future, I plan to make it fully portable and simplify its installation, but for now, it's entirely up to you.

You can find all the necessary libraries in `requirements.txt`, located in the project's root directory.

Currently, due to compatibility issues with AMD, the **TTS** and **STT** modules utilize the CPU, as they are lightweight and there's a significant performance difference between using them on the CPU or GPU. Therefore, you shouldn't have any problems with the GPU.

### 6. Use of AI

Okay, before anyone calls me a *vibe coder*, I'd like to clarify how I've used AI and that this project is educational in nature.

**All the project code is handwritten** (or typed).

I've used AI tools like **ChatGPT** to act as my teacher. They've taught me and helped me use libraries, troubleshoot compatibility issues, debug, unblock myself when I was stuck and didn't know how to proceed, establish a project path, etc.

They've basically acted as my teachers and, in fact, they've done quite well. Along with YouTube tutorials and online documentation, they've helped me understand many concepts.

All the architecture and code in *Nexus* were written by me from scratch.

### 7. Feedback

I'm completely open to **feedback, ideas, and constructive criticism**, as long as it's respectful.

However, I will not accept any pressure to update or make changes to Nexus. It's software you can download and use for free, and more importantly, it's a personal learning project.

So I don't see the need for anyone to pressure me to update it or change any of the architecture, etc. If you do this repeatedly, you'll probably be ignored or even banned.

Now, as I said at the beginning, if anyone wants to provide feedback, ideas for improving the architecture (I'm aiming for it to be as modular as possible), making the code more efficient, pointing out any security issues, etc., I'm completely open to it and would greatly appreciate it.

All I ask for is that you don't pressure me.