# Privacidad y limpieza

## Separación de datos

- Código: repositorio Git.
- Runtime y modelos: directorios descargados, excluidos de Git.
- Conversaciones, preferencias, caché y logs: directorio local de datos de PREPA AI.
- Credenciales: no se almacenan en equipos escolares compartidos.

## Niveles de limpieza

### 1. Limpiar datos de usuario

Elimina conversaciones, preferencias locales, caché y logs de PREPA AI. No elimina el código, Git, runtime ni modelos.

### 2. Salir y limpiar

Detiene los procesos iniciados por PREPA AI y luego ejecuta la limpieza de datos de usuario.

### 3. Eliminar copia local

Después de confirmación adicional, elimina la carpeta local del proyecto, incluida la carpeta `.git`, además del runtime y modelos que estén dentro de esa carpeta.

## Protecciones obligatorias

- Mostrar una lista exacta de rutas que se van a eliminar.
- Exigir confirmación explícita; para eliminar el repositorio, exigir escribir una frase de confirmación.
- Canonicalizar rutas y comprobar que están dentro de la raíz esperada.
- Rechazar rutas raíz, rutas vacías, unidades completas, carpetas de usuario y cualquier destino fuera de PREPA AI.
- No usar comodines amplios ni comandos de borrado sobre rutas construidas sin validar.
- No borrar el repositorio remoto de GitHub.
- No afirmar que el borrado es irrecuperable en SSD, copias de seguridad, antivirus, registros del sistema o sincronizaciones externas.

## Recomendación para equipos compartidos

No introducir contraseñas ni claves API personales. Utilizar la aplicación sin iniciar sesión en cuentas personales cuando sea posible. Al terminar, cerrar la aplicación y ejecutar la limpieza de datos.
