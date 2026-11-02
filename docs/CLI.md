# CLI de PREPA AI

## Estado

La CLI está modularizada y cuenta con pruebas unitarias. Para conversar necesita Windows, el ejecutable portable `PREPA-AI.exe` (o Python 3.10+), un binario compatible de `llama.cpp` y un modelo GGUF.

## Estructura del paquete

```text
PREPA-AI/
├─ PREPA-AI.exe
├─ prepa-ai.bat
├─ config.json
├─ config.json.example
├─ runtime/llama-server.exe
└─ models/modelo.gguf
```

Copia `config.json.example` a `config.json` si deseas cambiar los valores predeterminados. El lanzador intenta crear esa copia en el primer uso.

## Construir el ejecutable

En Windows con Python 3.10+:

```powershell
.\scripts\build.ps1
```

El paquete se prepara en `dist/package/`. También puedes descargar el artefacto de Windows desde la pestaña Actions del repositorio cuando termine **Build PREPA AI portable CLI**.

## Uso

Desde PowerShell o CMD:

```powershell
.\prepa-ai.bat
```

Opciones que funcionan antes de iniciar el motor:

- `PREPA-AI.exe --version`: mostrar versión.
- `PREPA-AI.exe --ayuda`: mostrar comandos.
- `PREPA-AI.exe --diagnostico`: comprobar requisitos y archivos locales.

Comandos durante la conversación:

- `/ayuda`: mostrar comandos.
- `/estado`: revisar si el motor responde.
- `/limpiar`: borrar la conversación de la memoria.
- `/modelo`: mostrar la ruta del modelo.
- `/diagnostico`: revisar archivos y requisitos.
- `/version`: mostrar versión.
- `/salir`: detener el motor y cerrar.

## Privacidad y red

El servidor se configura exclusivamente en `127.0.0.1`. La CLI no consulta proveedores de IA por internet. El historial se conserva únicamente en memoria; `/limpiar` lo reinicia y cerrar la aplicación lo descarta. No se escriben conversaciones ni claves API en disco.

## Pruebas

```powershell
py -3 -m unittest discover -s tests -v
```

Las pruebas unitarias no sustituyen una prueba real en Windows con llama.cpp y el modelo elegido. Consulta [componentes locales](ASSETS.md), [uso desde USB](USB.md) y [solución de problemas](TROUBLESHOOTING.md).
