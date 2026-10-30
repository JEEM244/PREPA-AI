$ErrorActionPreference = 'Stop'
Set-Location (Split-Path -Parent $PSScriptRoot)
py -3 -m compileall -q cli tests
if ($LASTEXITCODE -ne 0) { throw 'Falló compileall.' }
py -3 -m unittest discover -s tests -v
if ($LASTEXITCODE -ne 0) { throw 'Fallaron las pruebas unitarias.' }
Write-Host 'Verificación completada.'
