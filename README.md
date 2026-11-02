# PREPA AI

Asistente educativo portátil para Windows. La primera interfaz es la **CLI**, pensada para PowerShell y CMD, y para funcionar sin internet una vez que el motor y el modelo estén disponibles localmente.

> **Estado:** CLI modular, pruebas unitarias y compilación automática de un ejecutable Windows comprobadas en GitHub Actions. La ejecución real de inferencia todavía requiere incorporar y probar llama.cpp y un modelo GGUF compatible.

## Obtener el ejecutable

En GitHub abre **Actions → Build PREPA AI portable CLI**, selecciona la ejecución más reciente que haya terminado correctamente y descarga el artefacto `PREPA-AI-Windows-x64`.

También puedes construirlo en Windows con Python 3.10+:

```powershell
.\scripts\build.ps1
```

El paquete local se prepara en `dist/package/`.

## Preparar el motor y el modelo

1. Extrae una compilación confiable de llama.cpp dentro de `runtime/`, conservando sus DLL necesarias.
2. Coloca el modelo GGUF elegido dentro de `models/`.
3. Ejecuta `scripts/check-assets.ps1` para comprobar que los archivos estén presentes.
4. Ejecuta `prepa-ai.bat`. El lanzador crea `config.json` desde el ejemplo si hace falta.

Consulta [docs/ASSETS.md](docs/ASSETS.md) antes de descargar componentes.

## Comandos

Durante la conversación: `/ayuda`, `/estado`, `/limpiar`, `/modelo`, `/diagnostico`, `/version` y `/salir`.

Antes de iniciar el motor: `PREPA-AI.exe --version`, `PREPA-AI.exe --ayuda` o `PREPA-AI.exe --diagnostico`.

## Diseño y privacidad

- Motor local llama.cpp con modelo GGUF.
- API del motor enlazada únicamente a `127.0.0.1`.
- El historial vive solo en memoria y se descarta al cerrar.
- No se guardan claves API ni conversaciones en disco.
- No se intenta evadir filtros ni controles de la red escolar.

## Documentación

- [CLI](docs/CLI.md)
- [Componentes locales](docs/ASSETS.md)
- [Uso desde USB](docs/USB.md)
- [Portabilidad](docs/PORTABILITY.md)
- [Modelo local](docs/MODEL.md)
- [Solución de problemas](docs/TROUBLESHOOTING.md)
- [Privacidad](docs/PRIVACY.md)
- [Lista de verificación de v1.0](docs/RELEASE_CHECKLIST.md)

La compilación y las pruebas automáticas no sustituyen una prueba real de inferencia en el equipo escolar. La compatibilidad, velocidad y memoria disponible deben medirse en cada computadora.
