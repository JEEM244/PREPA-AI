# PREPA AI

Asistente educativo portátil para Windows. La primera interfaz es la **CLI**, pensada para PowerShell y CMD, y para funcionar sin internet una vez que el motor y el modelo estén disponibles localmente.

> **Estado:** CLI modular, comandos, diagnóstico, pruebas unitarias y flujo de compilación portable preparados. La ejecución real todavía requiere incorporar y probar llama.cpp y un modelo GGUF compatible.

## Inicio rápido

Consulta [docs/CLI.md](docs/CLI.md). Para preparar el paquete:

1. Ejecuta `scripts/build.ps1` en Windows con Python 3.10+.
2. El ejecutable se genera en `dist/package/`.
3. Coloca `llama-server.exe` en `runtime/` y un modelo GGUF en `models/`.
4. Copia `config.json.example` como `config.json`.
5. Ejecuta `prepa-ai.bat`.

También se define un flujo de compilación en GitHub Actions para Windows x64.

## Comandos

`/ayuda`, `/estado`, `/limpiar`, `/modelo`, `/diagnostico`, `/version` y `/salir`.

## Diseño y privacidad

- Motor local llama.cpp con modelo GGUF.
- API del motor enlazada únicamente a `127.0.0.1`.
- El historial vive solo en memoria y se descarta al cerrar.
- No se guardan claves API ni conversaciones en disco.
- No se intenta evadir filtros ni controles de la red escolar.

## Documentación

- [CLI](docs/CLI.md)
- [Uso desde USB](docs/USB.md)
- [Portabilidad](docs/PORTABILITY.md)
- [Modelo local](docs/MODEL.md)
- [Solución de problemas](docs/TROUBLESHOOTING.md)
- [Privacidad](docs/PRIVACY.md)
- [Lista de verificación de v1.0](docs/RELEASE_CHECKLIST.md)

La compatibilidad y el rendimiento deben probarse en cada equipo. El código y las pruebas no sustituyen una prueba real con el motor, el modelo y las computadoras escolares.
