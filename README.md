# PREPA AI

Asistente educativo portátil para Windows. La primera interfaz en desarrollo es la **CLI**, pensada para funcionar desde PowerShell o CMD sin depender de una página web.

> **Estado:** primera base del CLI añadida. Para conversar todavía requiere el runtime de llama.cpp y un modelo GGUF colocados localmente. El runtime portable de Python y el empaquetado como EXE están pendientes.

## Objetivos

- Ejecutar un modelo local GGUF mediante `llama.cpp`.
- Usar PREPA AI desde la consola, incluso cuando no haya internet.
- Mantener el historial de la sesión en memoria y no guardar conversaciones en disco por defecto.
- No subir modelos, conversaciones, claves API ni datos personales a Git.
- Permitir limpiar los datos de PREPA AI sin tocar archivos ajenos.
- No intentar evadir filtros o controles de la red escolar.

## CLI: primer arranque

Consulta [docs/CLI.md](docs/CLI.md) para ver requisitos, estructura de carpetas y comandos.

1. Coloca `llama-server.exe` en `runtime/`.
2. Coloca un modelo GGUF compatible en `models/`.
3. Copia `config.json.example` a `config.json`.
4. Ejecuta `prepa-ai.bat` desde PowerShell o CMD.

Comandos disponibles dentro de la CLI: `/ayuda`, `/estado`, `/limpiar` y `/salir`.

## Diseño técnico

- Motor: `llama.cpp` (CPU como opción base).
- Modelo inicial previsto: Qwen2.5 1.5B Instruct GGUF, sujeto a pruebas de rendimiento y licencia.
- CLI: Python 3.10+ en esta primera versión.
- Comunicación: API local de llama.cpp en `127.0.0.1`.
- Distribución: código en GitHub; runtime y modelos descargados por separado.

La aplicación todavía no incluye el runtime ni el modelo. El rendimiento debe probarse en cada computadora; no se garantiza que un modelo local funcione con fluidez en equipos escolares de recursos limitados.

## Privacidad

El historial de la primera versión solo vive en la memoria de la sesión y desaparece al cerrar PREPA AI. No se guarda en disco. El motor escucha únicamente en `127.0.0.1` y la aplicación no necesita internet para inferir una vez que el motor y el modelo están disponibles.

Consulta [docs/PRIVACY.md](docs/PRIVACY.md) para las reglas de limpieza y [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) para la arquitectura general.

## Seguridad

- No guardar claves API en el repositorio ni en equipos compartidos.
- No ejecutar comandos arbitrarios generados por el modelo.
- No abrir el servidor en la red local.
- No intentar evadir filtros o controles de la red escolar.
- Revisar las licencias del motor y del modelo antes de redistribuirlos.

## Licencia

Pendiente de elección. Los componentes de terceros conservan sus propias licencias.
