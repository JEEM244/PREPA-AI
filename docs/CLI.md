# CLI de PREPA AI

## Estado

Primera base del cliente de terminal. Requiere Windows, Python 3.10+ y un binario compatible de `llama.cpp` (`llama-server.exe`). El runtime portable para no depender de Python instalado sigue pendiente.

## Estructura esperada

```text
PREPA-AI/
├─ cli/prepa_ai.py
├─ runtime/llama-server.exe
├─ models/qwen2.5-1.5b-instruct-q4_k_m.gguf
├─ config.json
└─ prepa-ai.bat
```

Copia `config.json.example` como `config.json` y ajusta las rutas si cambian. El motor y el modelo no se incluyen en Git.

## Uso

Desde PowerShell o CMD:

```powershell
.\prepa-ai.bat
```

Comandos:

- `/ayuda`: muestra los comandos.
- `/estado`: consulta el estado del motor.
- `/limpiar`: borra el historial de la sesión actual (memoria RAM).
- `/salir`: detiene el motor iniciado por PREPA AI y cierra la CLI.

## Privacidad y red

El servidor se inicia en `127.0.0.1`, no se expone a otros equipos y no realiza llamadas a servicios de IA por internet. El historial actual vive solo en memoria y se pierde al cerrar. No se guardan conversaciones en disco en esta primera versión. No se ejecutan comandos escritos por el modelo.

Usa la herramienta únicamente donde esté permitido. No intenta saltarse bloqueos de red ni controles del equipo.
