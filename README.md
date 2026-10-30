# PREPA AI

Asistente educativo portátil para Windows. La primera interfaz es la **CLI**, pensada para PowerShell y CMD, y para funcionar sin internet una vez que el motor y el modelo estén disponibles localmente.

> **Estado:** primera versión de la CLI en desarrollo. El código base y las pruebas unitarias ya están añadidos. Todavía faltan el runtime portable, el binario de llama.cpp y el modelo GGUF.

## Objetivos

- Ejecutar un modelo GGUF local mediante `llama.cpp`.
- Conversar desde la terminal sin depender de páginas web.
- Mantener el historial solo en memoria durante la sesión.
- No subir modelos, conversaciones, claves API ni datos personales a Git.
- Ejecutarse desde una carpeta local o USB, sujeto a pruebas de compatibilidad.
- No intentar evadir filtros ni controles de la red escolar.

## Inicio

Consulta [docs/CLI.md](docs/CLI.md). Resumen:

1. Colocar `llama-server.exe` en `runtime/`.
2. Colocar un modelo GGUF compatible en `models/`.
3. Copiar `config.json.example` a `config.json`.
4. Ejecutar `prepa-ai.bat` desde CMD o PowerShell.

Comandos: `/ayuda`, `/estado`, `/limpiar`, `/modelo`, `/salir`.

## Diseño técnico

- Motor: `llama.cpp`.
- Modelo inicial previsto: Qwen2.5 1.5B Instruct GGUF, pendiente de validar.
- CLI: Python 3.10+ en desarrollo; runtime portable pendiente.
- Comunicación: API local en `127.0.0.1`.
- Sin dependencias Python externas para el cliente básico.

El rendimiento depende del equipo, el modelo y la compilación de llama.cpp. No se garantiza que funcione con fluidez en todas las computadoras escolares.

## Privacidad

El historial vive solo en memoria y se descarta al cerrar la aplicación. El servidor escucha exclusivamente en `127.0.0.1`. Consulta [docs/PRIVACY.md](docs/PRIVACY.md).

## Seguridad

- No guardar claves API en equipos compartidos.
- No ejecutar comandos generados por el modelo.
- No abrir el servidor en la red local.
- No intentar evadir filtros escolares.
- Revisar las licencias de los componentes de terceros antes de redistribuirlos.

## Pruebas

```powershell
py -3 -m unittest discover -s tests -v
```

GitHub Actions ejecuta las pruebas unitarias en Windows.
