# Problemas comunes

Esta guía reúne algunos errores que pueden aparecer al preparar PREPA-AI. La integración completa con llama.cpp todavía está pendiente, así que algunos casos son comprobaciones para la etapa de desarrollo y no una solución garantizada.

## No se encuentra Python

Para ejecutar las herramientas de desarrollo se necesita Python 3.10 o superior. El ejecutable portable se construye con el script del proyecto.

## No se encuentra llama-server

Comprueba que la descarga de llama.cpp corresponda a Windows x64 y que los archivos estén en la carpeta esperada. No mezcles el ejecutable con DLL de otra versión.

La conexión de este motor con la CLI todavía está pendiente.

## No se encuentra el modelo

Comprueba que el archivo GGUF esté completo y que el nombre coincida con la configuración. Revisa también que hayas descargado la cuantización que elegiste.

## El puerto está ocupado

Si estás probando el servidor local por separado, puede que otro proceso esté usando el puerto configurado. Cierra únicamente el proceso que hayas iniciado para esa prueba o usa otro puerto libre.

## El motor se cierra al iniciar

Puede ser un problema de compatibilidad entre la compilación de llama.cpp, el modelo o el procesador del equipo. Revisa que todos los archivos sean de la misma descarga y que el modelo no esté incompleto.

## Responde lento o aparece un error de memoria

El rendimiento depende de la RAM, el procesador, el tamaño del modelo y el contexto. Para medirlo, cierra programas que no necesites y registra qué equipo y configuración utilizaste.

## No hay internet

La meta es que la inferencia funcione sin conexión después de descargar los componentes. La descarga inicial sí necesita internet. El funcionamiento completo sin conexión todavía debe probarse desde PREPA-AI.
