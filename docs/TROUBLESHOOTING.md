# Solución de problemas

## No se encuentra Python

La versión actual necesita Python 3.10+ si no se está usando `PREPA-AI.exe`. La compilación portable con PyInstaller está preparada en el proyecto, pero debe probarse en Windows antes de distribuirse.

## No se encuentra llama-server

Comprueba que el archivo se llame exactamente `llama-server.exe` y esté en `runtime/`, o corrige `server_exe` en `config.json`.

## No se encuentra el modelo

Comprueba que el archivo GGUF esté en `models/` y que la ruta coincida con `model` en `config.json`.

## El puerto está ocupado

Cierra otra instancia de PREPA AI. Si el puerto sigue ocupado, cambia `port` en `config.json` por un valor libre entre 1024 y 65535.

## El motor se cierra al iniciar

Puede haber incompatibilidad entre el binario de llama.cpp, el modelo GGUF y las instrucciones de CPU del equipo. Comprueba que el archivo del modelo esté completo y usa una compilación compatible.

## Responde muy lento o falla por memoria

Reduce `context_size`, `max_tokens` o el tamaño del modelo. Cierra programas que no necesites. La velocidad depende del equipo.

## No hay internet

La inferencia local no requiere internet después de tener el runtime y el modelo descargados. La descarga inicial sí requiere una conexión autorizada.
