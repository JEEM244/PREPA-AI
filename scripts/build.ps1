$ErrorActionPreference = 'Stop'
Set-Location (Split-Path -Parent $PSScriptRoot)

Write-Host '== PREPA AI: pruebas =='
py -3 -m unittest discover -s tests -v
if ($LASTEXITCODE -ne 0) { throw 'Las pruebas fallaron; no se generará el ejecutable.' }

Write-Host '== PREPA AI: instalar herramienta de empaquetado =='
py -3 -m pip install -r requirements-build.txt
if ($LASTEXITCODE -ne 0) { throw 'No se pudo instalar PyInstaller.' }

Write-Host '== PREPA AI: construir ejecutable =='
py -3 -m PyInstaller --clean --noconfirm PREPA-AI.spec
if ($LASTEXITCODE -ne 0) { throw 'PyInstaller no pudo construir el ejecutable.' }

New-Item -ItemType Directory -Force -Path 'dist\package\runtime','dist\package\models' | Out-Null
Copy-Item 'dist\PREPA-AI.exe' 'dist\package\PREPA-AI.exe' -Force
Copy-Item 'prepa-ai.bat' 'dist\package\prepa-ai.bat' -Force
Copy-Item 'config.json.example' 'dist\package\config.json.example' -Force
Copy-Item 'README.md' 'dist\package\README.txt' -Force
Write-Host 'Listo: dist\package. Coloca llama-server.exe en runtime y el GGUF en models.'
