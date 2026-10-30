# CLI de PREPA AI

## Estado

La CLI tiene una estructura modular y pruebas unitarias. Para conversar requiere Windows, Python 3.10+ (o runtime portable pendiente), un binario compatible de `llama.cpp` y un modelo GGUF. Los binarios y pesos no se distribuyen dentro de Git.

## Estructura esperada

```text
PREPA-AI/
├─ cli/prepa_ai/       # aplicación, configuración, motor y chat
├─ runtime/            # llama-server.exe y futuro Python portable
├─ models/             # modelos GGUF
├─ config.json         # configuración local (no versionada)
├─ config.json.example
└─ prepa-ai.bat
```

Copia `config.json.example` a `config.json`. Coloca `llama-server.exe` en `runtime/` y el modelo GGUF en `models/`.

## Uso

Desde PowerShell o CMD:

```powershell
.\prepa-ai.bat
```

Comandos: `/ayuda`, `/estado`, `/limpiar`, `/modelo` y `/salir`. También reconoce `/help`, `/status`, `/clear` y `/exit`.

## Privacidad y red

El servidor se configura exclusivamente en `127.0.0.1`. La CLI no consulta proveedores de IA por internet. El historial se conserva únicamente en memoria; `/limpiar` lo reinicia y cerrar la aplicación lo descarta. No se escriben conversaciones ni claves API en disco.

## Pruebas

Desde la raíz:

```powershell
py -3 -m unittest discover -s tests -v
```

El motor real debe probarse en Windows con los binarios y el modelo compatibles que se usarán en la USB.
