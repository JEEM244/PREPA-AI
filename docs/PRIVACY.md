# Privacidad y limpieza

## Comportamiento de la versión actual

- Las conversaciones se mantienen en la memoria del proceso mientras la aplicación está abierta.
- `/limpiar` reinicia la lista de mensajes de la sesión.
- Al cerrar PREPA AI, la aplicación detiene el proceso local de llama.cpp que inició y termina la sesión.
- La aplicación no guarda conversaciones, logs de chat, caché de usuario ni claves API en archivos.
- Si se crea `config.json`, ese archivo conserva opciones de configuración, no el historial de conversación.
- Los archivos del programa, el runtime y el modelo GGUF permanecen en la carpeta o USB hasta que el usuario los retire.

El comando `/limpiar` reinicia el historial que mantiene la aplicación. No debe interpretarse como una garantía de borrado forense de memoria.

## Limpieza manual de la copia

Para retirar PREPA AI de una memoria USB o carpeta:

1. Cierra PREPA AI para que detenga el motor local.
2. Comprueba que estás seleccionando la copia correcta.
3. Elimina la carpeta de PREPA AI desde el Explorador de archivos, respetando las reglas del equipo o de la escuela.

Esto elimina la copia seleccionada, pero no garantiza el borrado irrecuperable de datos en SSD, copias de seguridad, antivirus, registros del sistema o sincronizaciones externas.

## Recomendaciones para equipos compartidos

- No introduzcas contraseñas, datos personales sensibles ni claves API.
- No guardes archivos personales dentro de la carpeta de PREPA AI.
- Usa únicamente componentes descargados de fuentes oficiales o confiables.
- Respeta las reglas de uso de los equipos y de la red escolar.

## Funciones que aún no existen

Esta versión no incluye un gestor de perfiles, carpeta de datos de usuario, borrado automático de archivos, ni una función para eliminar el proyecto completo. No ejecutes scripts de limpieza externos que no hayas revisado.
