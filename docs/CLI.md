# Uso de la CLI

Esta carpeta contiene la interfaz de PREPA-AI para PowerShell y CMD. La idea es que los comandos sean sencillos y que el programa pueda llevarse en una USB.

## Estado actual

La CLI tiene su estructura, comandos, pruebas y proceso para generar un ejecutable. **La conexión con llama.cpp y la respuesta de un modelo GGUF todavía no están terminadas ni probadas.** Por ahora no se debe considerar que el asistente ya puede mantener una conversación con un modelo local.

## Construir el ejecutable

En Windows con Python 3.10 o superior:

```powershell
.\scripts\build.ps1
```

El paquete se prepara en `dist/package/`. También se puede descargar el artefacto generado por GitHub Actions cuando la compilación termine correctamente.

## Comandos de inicio

Desde PowerShell o CMD:

```powershell
PREPA-AI.exe --version
PREPA-AI.exe --ayuda
PREPA-AI.exe --diagnostico
```

El lanzador para la carpeta portable es:

```powershell
.\prepa-ai.bat
```

## Comandos de la interfaz

La interfaz contempla estos comandos:

- `/ayuda`: mostrar la lista de comandos.
- `/estado`: revisar el estado del motor.
- `/limpiar`: limpiar la conversación de la sesión.
- `/modelo`: mostrar la configuración del modelo.
- `/diagnostico`: revisar archivos y requisitos.
- `/version`: mostrar la versión.
- `/salir`: cerrar la aplicación.

Algunos comandos dependen de que la integración con el motor esté terminada. Que aparezcan en la CLI no significa que la inferencia local ya funcione.

## Pruebas

```powershell
py -3 -m unittest discover -s tests -v
```

Estas pruebas revisan partes del programa, pero no sustituyen una prueba completa con llama.cpp y un modelo GGUF.

## Archivos relacionados

- [Preparar los componentes](ASSETS.md)
- [Uso desde USB](USB.md)
- [Portabilidad](PORTABILITY.md)
- [Privacidad](PRIVACY.md)
