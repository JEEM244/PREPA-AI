# Uso desde USB

## Preparación

1. Construye o descarga el paquete portable de PREPA AI.
2. Copia el paquete completo a una carpeta de la USB.
3. Coloca el ejecutable compatible de llama.cpp como `runtime/llama-server.exe`.
4. Coloca el modelo GGUF elegido dentro de `models/`.
5. Copia `config.json.example` como `config.json`.
6. Prueba todo en tu computadora antes de llevarlo a la escuela.

## En la computadora escolar

- Conecta la USB y abre la carpeta del proyecto.
- Ejecuta `prepa-ai.bat` desde CMD o PowerShell.
- No necesitas abrir una página web ni conectarte a un servicio de IA.
- Al terminar escribe `/salir`.

La ejecución depende de las reglas del equipo escolar. Si Windows, el antivirus o las políticas del laboratorio bloquean el programa, no intentes saltarte esos controles: solicita autorización al responsable.

## Privacidad

La conversación se mantiene en memoria y se descarta al cerrar. Evita escribir contraseñas, datos personales o información privada de otras personas. No guardes claves API en la USB.

## Rendimiento

El modelo se ejecuta usando los recursos de la computadora anfitriona. Prueba primero el modelo en el equipo menos potente donde planees usarlo.
