# Preparar los componentes locales

PREPA AI separa su código de los componentes grandes para mantener ligero el repositorio.

## Estructura

```text
PREPA-AI/
├─ PREPA-AI.exe
├─ prepa-ai.bat
├─ config.json
├─ runtime/
│  └─ llama-server.exe
└─ models/
   └─ qwen2.5-1.5b-instruct-q4_k_m.gguf
```

## Motor

Descarga una compilación de Windows x64 de llama.cpp desde su repositorio oficial de GitHub. Usa el archivo `llama-server.exe` de una compilación confiable y compatible con el procesador del equipo. No descargues ejecutables de páginas de terceros desconocidas.

La versión del motor debe anotarse junto con la fecha de descarga para poder reproducir las pruebas.

## Modelo

El modelo inicial propuesto es Qwen2.5 1.5B Instruct en formato GGUF, cuantización Q4_K_M. Descarga el archivo desde el repositorio oficial o una publicación de confianza que identifique claramente modelo, licencia y cuantización. Comprueba que la licencia permita el uso previsto.

No se incluye un enlace directo ni una versión fijada en esta guía porque las publicaciones pueden cambiar. No sustituyas el modelo por un archivo con el mismo nombre procedente de una fuente desconocida.

## Verificar archivos

Antes de llevarlos a la USB, calcula SHA-256 en PowerShell:

```powershell
Get-FileHash .\runtime\llama-server.exe -Algorithm SHA256
Get-FileHash .\models\qwen2.5-1.5b-instruct-q4_k_m.gguf -Algorithm SHA256
```

Guarda los hashes y la procedencia en tus notas locales. No es necesario subirlos al repositorio.

## Sin internet en la escuela

Descarga y prepara todos los componentes en una computadora con conexión autorizada. Después de copiarlos a la USB, PREPA AI puede ejecutar inferencia local sin internet, siempre que el equipo permita ejecutar el programa y tenga recursos suficientes.
