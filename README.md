# PREPA-AI

PREPA-AI es un asistente para usar desde la terminal de Windows. Quiero que pueda servir como apoyo para estudiar y trabajar en proyectos de la escuela, incluso cuando no haya internet.

Estoy empezando por una CLI para PowerShell y CMD. La intención es que se pueda llevar en una memoria USB y ejecutar en distintas computadoras.

## Estado actual

La estructura de la CLI, los comandos básicos, las pruebas y la compilación del ejecutable están preparados. **La respuesta real de un modelo todavía no está integrada ni comprobada**: falta conectar llama.cpp y probar un modelo GGUF.

Por eso, todavía no lo considero una IA local terminada.

## Comandos disponibles en la CLI

- `/ayuda`: muestra los comandos.
- `/estado`: consulta el estado.
- `/limpiar`: limpia la conversación actual.
- `/modelo`: muestra la configuración del modelo.
- `/diagnostico`: revisa componentes.
- `/version`: muestra la versión.
- `/salir`: cierra el programa.

## Preparar el proyecto

Se necesita Python 3.10 o superior para construirlo desde el código:

```powershell
.\scripts\build.ps1
```

El paquete se prepara en `dist/package/`.

Para usar un modelo local todavía hay que preparar llama.cpp y colocar un modelo GGUF compatible en la carpeta indicada. Los pasos están en [docs/ASSETS.md](docs/ASSETS.md).

## Qué quiero conseguir

- Que funcione sin conexión después de preparar el motor y el modelo.
- Que los archivos necesarios puedan ir junto al programa.
- Que el historial no se guarde automáticamente en disco.
- Que los comandos sean fáciles de usar desde la terminal.

## Documentación

- [Comandos](docs/CLI.md)
- [Archivos del motor y modelo](docs/ASSETS.md)
- [Uso desde USB](docs/USB.md)
- [Privacidad](docs/PRIVACY.md)
- [Problemas comunes](docs/TROUBLESHOOTING.md)

Es un proyecto en desarrollo. La velocidad y el funcionamiento dependerán del modelo, del equipo y de la memoria disponible.
