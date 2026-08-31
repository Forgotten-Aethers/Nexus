# Roadmap

`ROADMAP.md` written in both **English (EN)** and **Spanish (ES)**. If you wish to read in English, **please scroll down until you see "English (EN)" written.**

---

## Español (ES)

### Nexus 1.0 — Núcleo

Construcción de la base Nexus:

* LLM local funcional haciendo uso de Ollama.
* Sistema de conversaciones y persistencia.
* System prompt configurable desde un archivo `.txt` separado.
* Streaming de respuestas.
* Speech-to-Text mediante Faster-Whisper.
* Text-to-Speech mediante Piper.
* Comunicación entre LLM, STT y TTS.
* Sistema de colas para procesamientos de voz y texto.
* Launcher para iniciar Nexus.
* Uso de un sistema virtual de Python `.venv` (Cada ordenador debe instalarlo manualmente, es bastante sencillo con un tutorial).
* Facilitar parcialmente la instalación.
* Organización inicial del proyecto y repositorio.

**Objetivo:** Conseguir una base funcional con entrada de audio y salida de audio sobre la que trabajar.

---

### Nexus 1.1 — Interfaz y calidad de vida

Construcción de una interfaz que facilite trabajar con Nexus, además de proporcionar funciones de calidad de vida como borrar conversación, etc.

* Gestión visual de conversaciones.
* Configuración de Nexus desde la interfaz.
* Visualización del estado de los diferentes componentes.
* Mejoras de calidad de vida.
* Controles y opciones accesibles desde la interfaz.

**Objetivo:** Convertir Nexus en una aplicación propiamente dicha y no depender de la consola para utilizarlo.

---

### Nexus 1.2 — Herramientas

Capacidad de utilizar herramientas externas al modelo, por ejemplo; abrir aplicaciones.

* Sistema general de herramientas.
* Arquitectura para registrar y gestionar herramientas.
* Herramientas locales.
* Operaciones y utilidades del sistema.
* Ejecución controlada de determinadas acciones.
* Comunicación entre el LLM y las herramientas.

**Objetivo:** Permitir a Nexus realizar acciones.

---

### Nexus 1.3 — Internet

Incorporación de acceso controlado a información externa.

* Búsqueda en Internet.
* Consulta de páginas web.
* Obtención de información actualizada.
* Integración de la búsqueda como herramienta desactivable y activable.
* Procesamiento y síntesis de los resultados.
* Control de las fuentes y del contenido recibido.

**Objetivo:** Proporcionar a Nexus información en tiempo real.

---

### Nexus 1.4 — Voz

Actualización del sistema de voz.

* Optimización de Piper.
* Mejora de naturalidad y expresividad.
* Optimización de pausas y segmentación.
* Experimentación con diferentes modelos y voces.
* Integración de RVC como sistema de conversión de voz.
* Búsqueda de una voz con mayor sensación de naturalidad e inteligencia.

**Objetivo:** Conseguir que la voz de Nexus se aproxime a la de un asistente de ciencia ficción.

---

### Nexus 1.5 — Ingeniería, seguridad y optimización

Optimización y actualización de componentes internos.

* Reducir la creación innecesaria de archivos temporales, preferiblemente haciendo uso de RAM.
* Priorizar comunicación mediante memoria y estructuras internas cuando sea apropiado.
* Revisar la arquitectura de procesos.
* Reducir latencias.
* Eliminar código innecesario.
* Mejorar la eficiencia.
* Buscar soluciones más profesionales.
* Mejorar el manejo de errores.
* Revisar procesos y recursos.
* Implementar límites y permisos para las herramientas.
* Aumentar la seguridad del sistema.
* Evitar que Nexus pueda realizar acciones peligrosas accidentalmente.
* Mejorar la estabilidad general.

**Objetivo:** Conseguir una arquitectura eficiente, estable y segura.

---

### Nexus 1.6 — LLM

Mejoras al cerebro de Nexus.

* Reducir al máximo la latencia del LLM.
* Medir y optimizar el tiempo hasta el primer token.
* Optimizar generación y streaming.
* Permitir cambiar entre diferentes modelos.
* Gestión de modelos desde la interfaz.
* Permitir cambiar el System Prompt sin modificar el código.
* Comparar modelos utilizando pruebas específicas de Nexus.
* Buscar el modelo que ofrezca el mejor equilibrio entre calidad, velocidad y consumo de recursos.
* Optimización del System Prompt predeterminado.

**Objetivo:** Encontrar el mejor modelo predeterminado para Nexus, mayor configuración de su comportamiento, poder elegir entre modelos y aumentar velocidad.

---

### Nexus 1.7 — Memoria vectorial

Memoria a largo plazo entre conversaciones.

* Base de datos vectorial local.
* Recuperación semántica de recuerdos.
* Separación entre historial y memoria.
* Selección de información relevante para almacenar.
* Recuperación automática de recuerdos relacionados con la conversación actual.
* Gestión y eliminación de recuerdos.
* Mantener la memoria de Nexus de forma local.

**Objetivo:** Permitir que Nexus pueda recordar información relevante a largo plazo sin tener que introducir todo el historial de conversaciones en el contexto del LLM.

---

### Nexus 1.8 — STT

Puesta a punto del sistema de reconocimiento de voz.

* Optimización de Faster-Whisper.
* Reducción de latencia.
* Mejora del reconocimiento.
* Evaluación de diferentes modelos.
* Ajuste de parámetros.
* Optimización del procesamiento de audio.
* Investigación de aceleración mediante GPU.
* Mejora de la comunicación entre micrófono, STT y LLM.
* Procesamiento incremental cuando resulte viable.

**Objetivo:** Transcripción más rápida y precisa.

---

### Nexus 1.9 — Compatibilidad y distribución

Preparación de Nexus para funcionar en cualquier ordenador.

* Compatibilidad con diferentes sistemas operativos.
* Compatibilidad con diferentes arquitecturas de hardware.
* Detección automática del entorno.
* Selección del backend adecuado según el hardware.
* Diferentes builds cuando sea necesario.
* Instaladores específicos por plataforma.
* Dependencias independientes del sistema.
* Descarga automática de modelos.
* Configuración inicial automática.
* Distribución mediante GitHub.
* Separación entre código, dependencias, modelos, configuración y datos del usuario.
* Instalación y desinstalación limpias.

**Objetivo:** Que Nexus pueda ser trasladado a otro ordenador o descargado desde GitHub y preparado con el mínimo trabajo posible.

---

### Nexus 2.0 — Puesta a punto

* Comprobar que todos los elementos son modulares.
* Limpieza del código.
* Pruebas y estabilidad.
* Comprobar seguridad de Nexus.

**Objetivo:** Construir una base sólida sobre la que seguir desarrollando Nexus en un futuro (si llego hasta aquí, claro).

---

Los planes son conservar Nexus como un proyecto gratuito bajo la licencia actual hasta Nexus 2.0:

```text
Copyright (c) 2026 Forgotten Aethers - https://github.com/Forgotten-Aethers

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Commons Clause

The Software is provided under the MIT License above, with the
following additional condition:

The Software is provided to you by the Licensor under the License, as defined below, subject to the following condition.

Without limiting other conditions in the License, the grant of rights under the License will not include, and the License does not grant to you, the right to Sell the Software.

For purposes of the foregoing, “Sell” means practicing any or all of the rights granted to you under the License to provide to third parties, for a fee or other consideration (including without limitation fees for hosting or consulting/ support services related to the Software), a product or service whose value derives, entirely or substantially, from the functionality of the Software. Any license notice or attribution required by the License must also include this Commons Clause License Condition notice.
```

Después de Nexus 2.0 el futuro del proyecto es incierto, podría llegar a intentar comercializarlo, abandonarlo o simplemente seguir desarrollándolo bajo la misma licencia y criterio.

## English (EN)

### Nexus 1.0 — Core

Building the foundation of Nexus:

* Functional local LLM using Ollama.
* Conversation and persistence system.
* Configurable system prompt from a separate `.txt` file.
* Response streaming.
* Speech-to-Text using Faster-Whisper.
* Text-to-Speech using Piper.
* Communication between LLM, STT, and TTS.
* Queue system for voice and text processing.
* Launcher for starting Nexus.
* Use of a Python virtual environment `.venv` (Each computer must install it manually; it is fairly simple with a tutorial).
* Partially streamlined installation.
* Initial project and repository organization.

**Goal:** Build a functional foundation with audio input and audio output to serve as a basis for further development.

---

### Nexus 1.1 — Interface and Quality of Life

Building an interface that makes Nexus easier to work with, while also providing quality-of-life features such as deleting conversations, etc.

* Visual conversation management.
* Nexus configuration through the interface.
* Status display for the different components.
* Quality-of-life improvements.
* Controls and options accessible from the interface.

**Goal:** Turn Nexus into a proper application rather than relying on the console to use it.

---

### Nexus 1.2 — Tools

Ability to use tools external to the model, for example; opening applications.

* General-purpose tool system.
* Architecture for registering and managing tools.
* Local tools.
* System operations and utilities.
* Controlled execution of specific actions.
* Communication between the LLM and tools.

**Goal:** Allow Nexus to perform actions.

---

### Nexus 1.3 — Internet

Introducing controlled access to external information.

* Internet search.
* Web page retrieval.
* Access to up-to-date information.
* Integration of search as a tool that can be enabled and disabled.
* Processing and synthesis of search results.
* Control over the sources and content received.

**Goal:** Provide Nexus with real-time information.

---

### Nexus 1.4 — Voice

Updating the voice system.

* Piper optimization.
* Improved naturalness and expressiveness.
* Optimization of pauses and segmentation.
* Experimentation with different models and voices.
* Integration of RVC as a voice conversion system.
* Searching for a voice with a greater sense of naturalness and intelligence.

**Goal:** Make Nexus's voice resemble that of a science-fiction assistant.

---

### Nexus 1.5 — Engineering, Security, and Optimization

Optimization and modernization of internal components.

* Reduce unnecessary creation of temporary files, preferably by making use of RAM.
* Prioritize communication through memory and internal data structures when appropriate.
* Review process architecture.
* Reduce latency.
* Remove unnecessary code.
* Improve efficiency.
* Look for more professional solutions.
* Improve error handling.
* Review processes and resource usage.
* Implement limits and permissions for tools.
* Increase system security.
* Prevent Nexus from accidentally performing dangerous actions.
* Improve overall stability.

**Goal:** Build an efficient, stable, and secure architecture.

---

### Nexus 1.6 — LLM

Improvements to Nexus's brain.

* Minimize LLM latency.
* Measure and optimize time to first token.
* Optimize generation and streaming.
* Allow switching between different models.
* Model management through the interface.
* Allow changing the System Prompt without modifying the code.
* Compare models using Nexus-specific benchmarks.
* Find the model that offers the best balance between quality, speed, and resource consumption.
* Optimize the default System Prompt.

**Goal:** Find the best default model for Nexus, provide greater control over its behavior, allow switching between models, and increase speed.

---

### Nexus 1.7 — Vector Memory

Long-term memory across conversations.

* Local vector database.
* Semantic memory retrieval.
* Separation between conversation history and memory.
* Selection of relevant information to store.
* Automatic retrieval of memories related to the current conversation.
* Memory management and deletion.
* Keep Nexus's memory stored locally.

**Goal:** Allow Nexus to remember relevant information in the long term without having to include the entire conversation history in the LLM's context.

---

### Nexus 1.8 — STT

Fine-tuning the speech recognition system.

* Faster-Whisper optimization.
* Reduced latency.
* Improved recognition.
* Evaluation of different models.
* Parameter tuning.
* Audio processing optimization.
* Research into GPU acceleration.
* Improved communication between the microphone, STT, and LLM.
* Incremental processing whenever viable.

**Goal:** Faster and more accurate transcription.

---

### Nexus 1.9 — Compatibility and Distribution

Preparing Nexus to run on any computer.

* Compatibility with different operating systems.
* Compatibility with different hardware architectures.
* Automatic environment detection.
* Selection of the appropriate backend based on the hardware.
* Different builds when necessary.
* Platform-specific installers.
* System-independent dependencies.
* Automatic model downloads.
* Automatic initial configuration.
* Distribution through GitHub.
* Separation between code, dependencies, models, configuration, and user data.
* Clean installation and uninstallation.

**Goal:** Allow Nexus to be moved to another computer or downloaded from GitHub and set up with as little manual work as possible.

---

### Nexus 2.0 — Finalization

* Ensure that all components are modular.
* Code cleanup.
* Testing and stability.
* Verify Nexus's security.

**Goal:** Build a solid foundation on which to continue developing Nexus in the future (if I actually make it this far, of course).

---

The plan is to keep Nexus as a free project under the current license until Nexus 2.0:

```text

Copyright (c) 2026 Forgotten Aethers - [https://github.com/Forgotten-Aethers](https://github.com/Forgotten-Aethers)

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Commons Clause

The Software is provided under the MIT License above, with the

following additional condition:

The Software is provided to you by the Licensor under the License, as defined below, subject to the following condition.

Without limiting other conditions in the License, the grant of rights under the License will not include, and the License does not grant to you, the right to Sell the Software.

For purposes of the foregoing, “Sell” means practicing any or all of the rights granted to you under the License to provide to third parties, for a fee or other consideration (including without limitation fees for hosting or consulting/ support services related to the Software), a product or service whose value derives, entirely or substantially, from the functionality of the Software. Any license notice or attribution required by the License must also include this Commons Clause License Condition notice.

```

After Nexus 2.0, the future of the project is uncertain. I may eventually try to commercialize it, abandon it, or simply continue developing it under the same license and principles.