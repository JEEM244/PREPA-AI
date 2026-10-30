# Modelo local

## Modelo inicial propuesto

El proyecto contempla comenzar con un modelo instruct pequeño de la familia Qwen2.5, cuantizado en GGUF (por ejemplo Q4_K_M). Es una propuesta para pruebas, no una garantía de compatibilidad ni una descarga incluida en el repositorio.

## Antes de elegir

- Verifica que el archivo sea GGUF y que la versión de llama.cpp lo soporte.
- Revisa la licencia y las condiciones del repositorio oficial del modelo.
- Comprueba el tamaño del archivo y el espacio libre de la USB.
- Prueba el modelo en la computadora menos potente que planeas usar.
- Evita descargas de procedencia desconocida.

## Memoria y velocidad

La RAM necesaria depende del tamaño del modelo, la cuantización, el contexto y el motor. PREPA AI usa un contexto inicial moderado y limita la cantidad de turnos enviados en cada solicitud. Si hay errores de memoria, reduce el contexto o utiliza un modelo más pequeño.

No se promete una velocidad concreta en computadoras escolares. Las pruebas reales en los equipos destino son obligatorias.
