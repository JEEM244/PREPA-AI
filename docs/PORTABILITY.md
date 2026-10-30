# Portabilidad de PREPA AI

## Componentes separados

- `PREPA-AI.exe`: cliente CLI y runtime Python empaquetado por PyInstaller.
- `runtime/llama-server.exe`: motor llama.cpp, descargado aparte.
- `models/*.gguf`: pesos del modelo, descargados aparte.
- `config.json`: configuración local de la carpeta portable.

## Por qué no se incluye el motor ni el modelo

El motor y los modelos pueden ocupar mucho espacio, tienen ciclos de actualización y licencias independientes. No se deben versionar en Git. Revisa el origen, la integridad y las condiciones de uso de cada descarga.

## Compatibilidad

El ejecutable de PREPA AI se construye para Windows x64. La compatibilidad del motor depende de la compilación y de las capacidades de CPU. El paquete debe probarse en el equipo destino.
