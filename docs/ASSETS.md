# Preparar los componentes locales

PREPA AI separa su código de los componentes grandes para mantener ligero el repositorio.

## Componentes elegidos para la primera prueba

| Componente | Selección | Tamaño / licencia |
|---|---|---|
| Motor | llama.cpp, Windows x64 (CPU) | Descargar ZIP oficial |
| Modelo | Qwen2.5-1.5B-Instruct-GGUF, Q4_K_M | Aproximadamente 1.12 GB; Apache 2.0 |

Enlaces oficiales:

- [Publicaciones de llama.cpp](https://github.com/ggml-org/llama.cpp/releases) — elegir **Windows x64 (CPU)**, no CUDA ni ARM.
- [Modelo Qwen2.5 1.5B Instruct GGUF](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF).
- [Descarga directa del archivo Q4_K_M](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/qwen2.5-1.5b-instruct-q4_k_m.gguf).

La publicación de llama.cpp cambia con el tiempo. Al descargar, anota el tag o versión exacta para poder repetir la prueba. La página oficial muestra distintas compilaciones de Windows; para PREPA AI se empieza con CPU x64 por compatibilidad con equipos sin GPU dedicada.

## Estructura

```text
PREPA-AI/
├─ PREPA-AI.exe
├─ prepa-ai.bat
├─ config.json
├─ runtime/
│  ├─ llama-server.exe
│  └─ DLL que incluya la misma compilación
└─ models/
   └─ qwen2.5-1.5b-instruct-q4_k_m.gguf
```

## Motor

Descarga el ZIP Windows x64 (CPU) desde las publicaciones oficiales de llama.cpp. Extrae el contenido necesario de la misma publicación dentro de `runtime/`; no copies solamente `llama-server.exe` si la compilación incluye DLL necesarias junto a él.

No mezcles DLL de distintas versiones ni uses ejecutables de páginas de terceros desconocidas.

## Modelo

El modelo seleccionado para la primera prueba es Qwen2.5 1.5B Instruct en formato GGUF, cuantización Q4_K_M. La ficha oficial identifica la licencia Apache 2.0 y publica el archivo Q4_K_M de aproximadamente 1.12 GB.

El archivo no se incluye en Git ni en el paquete de compilación del CLI. Descárgalo en una conexión autorizada y consérvalo en la carpeta `models/`.

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

Guarda los hashes, la procedencia y la versión del motor en tus notas locales. No es necesario subirlos al repositorio.

## Sin internet en la escuela

Descarga y prepara todos los componentes en una computadora con conexión autorizada. Después de copiarlos a la USB, PREPA AI puede ejecutar inferencia local sin internet, siempre que el equipo permita ejecutar el programa y tenga recursos suficientes.
