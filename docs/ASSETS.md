# Preparar los componentes locales

PREPA AI separa su código de los componentes grandes para mantener ligero el repositorio.

## Estructura

```text
PREPA-AI/
├─ PREPA-AI.exe
├─ prepa-ai.bat
├─ config.json
├─ runtime/
│  ├─ llama-server.exe
│  └─ archivos DLL que incluya la misma compilación
└─ models/
   └─ qwen2.5-1.5b-instruct-q4_k_m.gguf
```

## Motor

Descarga una compilación de Windows x64 de llama.cpp desde su repositorio oficial de GitHub. Extrae el contenido necesario de la misma publicación dentro de `runtime/`; no copies solamente `llama-server.exe` si la compilación incluye DLL necesarias junto a él.

Usa una compilación confiable y compatible con el procesador del equipo. No descargues ejecutables de páginas de terceros desconocidas. Anota la versión del motor y la fecha de descarga para poder reproducir las pruebas.

## Modelo

El modelo inicial propuesto es Qwen2.5 1.5B Instruct en formato GGUF, cuantización Q4_K_M. Descarga el archivo desde el repositorio oficial o una publicación de confianza que identifique claramente modelo, licencia y cuantización. Comprueba que la licencia permita el uso previsto.

No se incluye un enlace directo ni una versión fijada en esta guía porque las publicaciones pueden cambiar. No sustituyas el modelo por un archivo con el mismo nombre procedente de una fuente desconocida.

## Verificar archivos

Después de extraer los componentes, ejecuta:

```powershell
.\scripts\check-assets.ps1
```

También puedes calcular SHA-256 manualmente:

```powershell
Get-FileHash .\runtime\llama-server.exe -Algorithm SHA256
Get-FileHash .\models\qwen2.5-1.5b-instruct-q4_k_m.gguf -Algorithm SHA256
```

Guarda los hashes y la procedencia en tus notas locales. No es necesario subirlos al repositorio.

## Sin internet en la escuela

Descarga y prepara todos los componentes en una computadora con conexión autorizada. Después de copiarlos a la USB, PREPA AI puede ejecutar inferencia local sin internet, siempre que el equipo permita ejecutar el programa y tenga recursos suficientes.
