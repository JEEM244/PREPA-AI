# PREPA AI

Asistente educativo portátil para Windows, con dos interfaces (CLI y web) que comparten un único motor local.

> **Estado:** estructura inicial en diseño. Todavía no es una aplicación funcional ni incluye ejecutables o modelos.

## Objetivos

- Ejecutar un modelo local GGUF mediante `llama.cpp`.
- Compartir el mismo servidor local entre la CLI y la interfaz web.
- Mantener conversaciones, preferencias y caché en almacenamiento local.
- No subir modelos, conversaciones, claves API ni datos personales a Git.
- Permitir limpiar los datos de PREPA AI de la carpeta de trabajo actual.
- Ofrecer proveedores online opcionales únicamente cuando la red los permita y su uso esté autorizado.

## Diseño previsto

- Motor: `llama.cpp` (CPU como opción base).
- Modelo inicial: Qwen2.5 1.5B Instruct GGUF, sujeto a pruebas de rendimiento y licencia.
- Backend y CLI: Python.
- Interfaz web: HTML, CSS y JavaScript servidos localmente.
- Comunicación: API HTTP en loopback (`127.0.0.1`).
- Distribución: código en GitHub; runtime y modelos descargados por separado.

## Requisitos previstos

- Windows 10/11 x64.
- Git para Windows.
- Permiso para ejecutar aplicaciones portátiles en el equipo.
- Espacio suficiente para el runtime y el modelo.
- Python no será requisito global: se evaluará incluir un runtime portable o distribuir un ejecutable.

La compatibilidad y el rendimiento se deben probar en cada equipo. No se garantiza que un modelo local funcione con fluidez en computadoras escolares de recursos limitados.

## Inicio del desarrollo

Consulta [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) para conocer los componentes y [docs/PRIVACY.md](docs/PRIVACY.md) para el comportamiento de limpieza.

## Privacidad y limpieza

PREPA AI debe guardar los datos de usuario fuera del repositorio Git, en un directorio local controlado por la aplicación. La limpieza debe:

1. detener únicamente los procesos iniciados por PREPA AI;
2. mostrar qué datos se eliminarán;
3. pedir confirmación explícita;
4. borrar solamente rutas pertenecientes al directorio de datos de PREPA AI;
5. conservar el código y el repositorio por defecto.

La opción de desinstalación podrá borrar también la copia local del proyecto, pero nunca debe borrar el repositorio remoto de GitHub ni archivos ajenos al proyecto.

## Seguridad

- No guardar claves API en el repositorio ni en equipos compartidos.
- No ejecutar comandos arbitrarios generados por el modelo.
- No abrir el servidor en la red local: usar `127.0.0.1`.
- No intentar evadir filtros o controles de la red escolar.
- Revisar las licencias del motor, modelo y dependencias antes de redistribuirlos.

## Licencia

Pendiente de elección. Los componentes de terceros conservan sus propias licencias.
