# Modelo para las primeras pruebas

Para la primera prueba de PREPA-AI elegí **Qwen2.5-1.5B-Instruct-GGUF, Q4_K_M**.

Lo elegí como punto de partida porque es un modelo relativamente pequeño comparado con otros modelos de lenguaje. Aun así, no significa que vaya a funcionar rápido en cualquier computadora.

## Datos del modelo

- Archivo: `qwen2.5-1.5b-instruct-q4_k_m.gguf`
- Formato: GGUF.
- Uso previsto: ejecución local con llama.cpp.
- Licencia indicada en su ficha: Apache 2.0.
- Fuente: [Qwen2.5 1.5B Instruct GGUF](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF).

Revisa la página del modelo antes de descargarlo, porque el tamaño y los archivos disponibles pueden cambiar.

## Antes de probarlo

- Descarga desde la página oficial.
- Revisa que el archivo sea la cuantización Q4_K_M.
- Comprueba que tengas espacio suficiente.
- Guarda el nombre de la versión y el origen del archivo.
- No uses copias de páginas desconocidas.

## Memoria y velocidad

El uso de RAM depende del modelo, la cuantización, el contexto y el motor. También cambia según la computadora.

La configuración inicial del proyecto contempla un contexto moderado, pero todavía falta conectar el modelo y medir el consumo real en los equipos donde se quiera usar.

## Estado

La selección del modelo ya está documentada, pero la inferencia local todavía no está integrada ni validada desde PREPA-AI. No hay que confundir tener el archivo GGUF con tener el asistente funcionando.
