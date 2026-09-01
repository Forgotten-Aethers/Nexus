# Guía de instalación

`Guía de instalación.md` written in both **English (EN)** and **Spanish (ES)**. If you wish to read in English, **please scroll down until you see "English (EN)" written.**

---

## Español (ES)

Nexus actualmente solo funciona en Windows, aunque pronto debería de funcionar tambien para Linux, te invito a modificar el código y buscar la solución, ya que el supuesto problema de compatibilidad (No lo he probado en Linux todavía) seguramente provenga de la librería `sys`. Debería ser fácil de solucionar. Si logras hacerlo, sigue estos pasos adaptando los comandos necesarios a la terminar de Linux.

Suponiendo que no haya problemas de compatibilidad, instalar Nexus 1.0 debería de ser bastante sencillo si sigues los siguientes pasos:

1. Lo primero que debes crear es un entorno virtual de python, preferiblemente 3.13.15. Para realizarlo, esta guía hará uso de una herramienta de código abierto llamada [uv](https://docs.astral.sh/uv/) desarrollada por Astral, no te preocupes, es ligera y te será de utilidad en un futuro.

    Deberás de abrir powershell y usar
    
    `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
`

    Una vez instalado, deberás de abrir la terminal dentro de la carpeta del proyecto y usar el siguiente comando
    
    `uv venv --python 3.13.15`

2. Ahora vamos a instalar las librerías necesarias desde esa misma terminal:

    Lo primero es activar el nuevo entorno virtual, desde la misma terminal, ejecuta
    
    `.venv\Scripts\activate`

    Ahora vamos a instalar las librerías en si mismas, ejecuta esto:
    
    `pip install -r docs/requirements.txt`

Y eso sería todo!

## English (EN)

Nexus currently only works on Windows, although it should soon also work on Linux. I invite you to modify the code and look for a solution, as the supposed compatibility issue (I haven't tested it on Linux yet) most likely comes from the `sys` library. It should be easy to fix. If you manage to get it working, follow these steps while adapting the necessary commands to the Linux terminal.

Assuming there are no compatibility issues, installing Nexus 1.0 should be fairly simple if you follow these steps:

1. The first thing you need to do is create a Python virtual environment, preferably using Python 3.13.15. To do this, this guide will use an open-source tool called [uv](https://docs.astral.sh/uv/) developed by Astral. Don't worry, it's lightweight and will be useful to you in the future.

   Open PowerShell and run:

   `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

   Once it is installed, open a terminal inside the project folder and run the following command:

   `uv venv --python 3.13.15`

2. Now let's install the required libraries from the same terminal.

   First, activate the new virtual environment by running:

   `.venv\Scripts\activate`

   Now install the required libraries by running:

   `pip install -r docs/requirements.txt`

And that's it!
