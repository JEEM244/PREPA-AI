# PREPA-AI desde una USB

La idea del proyecto es poder llevarlo en una memoria USB y usarlo en distintas computadoras con Windows. Esta parte todavía necesita pruebas en equipos diferentes.

## Preparación planeada

Cuando la integración del modelo esté lista, el paquete deberá incluir:

1. El ejecutable de PREPA-AI.
2. El lanzador `prepa-ai.bat`.
3. La carpeta `runtime/` con la compilación compatible de llama.cpp.
4. La carpeta `models/` con el modelo GGUF.
5. El archivo de configuración local.

El motor y el modelo se descargan por separado. Consulta [ASSETS.md](ASSETS.md) para revisar las fuentes y los archivos elegidos.

## Estado actual

La CLI y su compilación tienen pruebas, pero la conversación con un modelo local todavía no está terminada. Antes de usar esta guía como procedimiento final, falta conectar llama.cpp y probar el paquete completo en Windows.

## En una computadora de la escuela

Primero hay que confirmar que las reglas del laboratorio permitan ejecutar programas desde una USB. Si Windows, el antivirus o las políticas del equipo bloquean la aplicación, no intentes saltarte esos controles; pregunta al responsable del laboratorio.

## Privacidad

No escribas contraseñas, datos personales ni información privada de otras personas. La idea es que las conversaciones se mantengan en la sesión y no se guarden como historial, pero ese comportamiento debe volver a comprobarse cuando se integre el motor.

## Pruebas pendientes

- Probar en una computadora sin Python instalado.
- Probar después de copiar el paquete a una USB.
- Comprobar el funcionamiento sin internet después de descargar los componentes.
- Medir el uso de memoria y la velocidad en equipos de distintas capacidades.
