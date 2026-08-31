# Registro de errores

`Registro de errores.md` written in both **English (EN)** and **Spanish (ES)**. If you wish to read in English, **please scroll down until you see "English (EN)" written.**

---

## Español (ES)

### Errores pendientes (Bugs Activos)

* **[BUG-002]:** La conversación puede quedar inconsistente si Ollama produce una excepción durante la generación de la respuesta.
    * **Existencia:** Teórica
    * **Descubierto:** 24/08/2026
    * **Versión:** 1.0
    * **Estado:** Pendiente
    * **Descripción:** El mensaje del usuario se guarda antes de llamar a `ollama.chat()`. Si la generación falla, la conversación queda almacenada sin la respuesta del asistente.
    * **Solución Temporal:** Entrar a la conversación en `conversations` dentro de `data`, en `LLM` y borrar el input del usuario. Después carga la conversación y copia el mismo input.

* **[BUG-003]:** El proceso STT finaliza si Whisper lanza una excepción no controlada.
    * **Existencia:** Teórica
    * **Descubierto:** 24/08/2026
    * **Versión:** 1.0
    * **Estado:** Pendiente
    * **Descripción:** Una excepción en `model.transcribe()` termina el proceso STT, requiriendo reiniciar Nexus.
    * **Solución Temporal:** Cerrar y abrir Nexus (Desde el launcher).

* **[BUG-004]:** El proceso TTS finaliza si Piper lanza una excepción no controlada.
    * **Existencia:** Teórica
    * **Descubierto:** 24/08/2026
    * **Versión:** 1.0
    * **Estado:** Pendiente
    * **Descripción:** Una excepción durante la síntesis de voz termina el proceso TTS.
    * **Solución Temporal:** Cerrar y abrir Nexus (Desde el launcher).

* **[BUG-005]:** Posible pérdida de texto en la cola TTS por acceso concurrente entre LLM y TTS.

    * **Existencia:** Teórica
    * **Descubierto:** 24/08/2026
    * **Versión:** 1.0
    * **Estado:** Pendiente
    * **Descripción:** Cuando TTS sobreescribe el archivo, en un momento dado, LLM puede haber escrito algo que TTS no haya registrado en `resto`.
    * **Solución Temporal:** Sin solución temporal.

### Errores solucionados (Historial)

* **[BUG-001]:** Procesos duplicados en segundo plano al cerrar el launcher desde la "X".
    * **Existencia:** Comprobada
    * **Descubierto:** 24/08/2026
    * **Fecha:** 24/08/2026
    * **Versión:** 1.0
    * **Solución:** Se implementó la librería nativa `atexit` para registrar la función `cleaning_at_exit()`, forzando el `.terminate()` y `.wait()` de todos los subprocesos de la lista.

---

## English (EN)

### Pending Errors (Active Bugs)

* **[BUG-002]:** Conversation may become inconsistent if Ollama raises an exception while generating a response.
    * **Existence:** Theoretical
    * **Discovered:** 24/08/2026
    * **Version:** 1.0
    * **Status:** Pending
    * **Description:** The user's message is saved before calling `ollama.chat()`. If generation fails, the conversation is stored without the assistant's reply.
    * **Temporary Solution:** Open the conversation in `conversations` inside `data`, under `LLM`, and delete the user's input. Then load the conversation and copy the same input again.

* **[BUG-003]:** The STT process terminates if Whisper raises an unhandled exception.
    * **Existence:** Theoretical
    * **Discovered:** 24/08/2026
    * **Version:** 1.0
    * **Status:** Pending
    * **Description:** An exception inside `model.transcribe()` terminates the STT process.
    * **Temporary Solution:** Close and reopen Nexus (from the launcher).

* **[BUG-004]:** The TTS process terminates if Piper raises an unhandled exception.
    * **Existence:** Theoretical
    * **Discovered:** 24/08/2026
    * **Version:** 1.0
    * **Status:** Pending
    * **Description:** An exception during speech synthesis terminates the TTS process.
    * **Temporary Solution:** Close and reopen Nexus (from the launcher).

* **[BUG-005]:** Possible loss of text in the TTS queue due to concurrent access between LLM and TTS.

    * **Existence:** Theoretical
    * **Discovered:** 24/08/2026
    * **Version:** 1.0
    * **Status:** Pending
    * **Description:** When TTS overwrites the file, at a certain point, the  LLM may have written something that TTS has not yet registered in `resto`.
    * **Temporary Solution:** No temporary solution.

### Resolved Errors (History)

* **[BUG-001]:** Duplicate background processes when closing the launcher using the "X".
    * **Existence:** Verified
    * **Discovered:** 08/24/2026
    * **Date:** 08/24/2026
    * **Version:** 1.0
    * **Solution:** Implemented the native `atexit` library to register the `cleaning_at_exit()` function, forcing `.terminate()` and `.wait()` on all subprocesses in the list.

