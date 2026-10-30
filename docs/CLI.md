# CLI de PREPA AI

## Estado

La CLI está modularizada y cuenta con pruebas unitarias. Para conversar necesita Windows, el ejecutable portable `PREPA-AI.exe` (o Python 3.10+), un binario compatible de `llama.cpp` y un modelo GGUF. El ejecutable de PREPA AI se puede construir con PyInstaller o mediante el flujo de GitHub Actions para Windows.

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

Copia `config.json.example` a `config.json`. Coloca `llama-server.exe` en `runtime/` y el modelo GGUF en `models/`. Los binarios y pesos no se guardan en Git.

## Construir el ejecutable

En Windows con Python 3.10+:

```powershell
.\scripts\build.ps1
```

El paquete se prepara en `dist/package/`. También puedes ejecutar manualmente el workflow **Build PREPA AI portable CLI** desde la pestaña Actions del repositorio y descargar el artefacto de Windows.

## Uso

Desde PowerShell o CMD:

```powershell
.\prepa-ai.bat
```

Comandos disponibles:

- `/ayuda`: mostrar comandos.
- `/estado`: revisar si el motor responde.
- `/limpiar`: borrar la conversación de la memoria.
- `/modelo`: mostrar la ruta del modelo.
- `/diagnostico`: revisar archivos y requisitos.
- `/version`: mostrar la versión.
- `/salir`: detener el motor y cerrar.

## Privacidad y red

El servidor se configura exclusivamente en `127.0.0.1`. La CLI no consulta proveedores de IA por internet. El historial se conserva únicamente en memoria; `/limpiar` lo reinicia y cerrar la aplicación lo descarta. No se escriben conversaciones ni claves API en disco.

## Pruebas

Desde la raíz:

```powershell
py -3 -m unittest discover -s tests -v
```

Las pruebas unitarias no sustituyen una prueba real en Windows con llama.cpp y el modelo elegido. Consulta también [Uso desde USB](USB.md), [Portabilidad](PORTABILITY.md) y [Solución de problemas](TROUBLESHOOTING.md).
