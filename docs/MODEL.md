# Modelo local

## Modelo inicial seleccionado

**Qwen2.5-1.5B-Instruct-GGUF — Q4_K_M**

- Repositorio: [Qwen en Hugging Face](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF)
- Archivo: `qwen2.5-1.5b-instruct-q4_k_m.gguf`
- Tamaño publicado: aproximadamente 1.12 GB.
- Licencia indicada en la ficha: Apache 2.0.
- Formato: GGUF, para uso con llama.cpp.

La selección es un punto de partida para probar en computadoras con memoria limitada; no garantiza una velocidad determinada ni que todos los equipos escolares puedan ejecutarlo.

## Antes de descargar

- Verifica que estés en el repositorio oficial del modelo.
- Comprueba el nombre y la cuantización Q4_K_M.
- Revisa la licencia y las condiciones de uso.
- Asegúrate de tener espacio suficiente en la USB.
- No uses copias de origen desconocido.

## Memoria y velocidad

La RAM necesaria depende del modelo, la cuantización, el contexto y el motor. PREPA AI inicia con un contexto moderado de 2048 tokens y limita el historial enviado en cada solicitud. Si el equipo presenta errores de memoria, habrá que probar un modelo más pequeño o reducir el contexto.

No se promete una velocidad concreta. Las pruebas reales en los equipos destino son obligatorias.
