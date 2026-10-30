@echo off
setlocal
cd /d "%~dp0"
set "PYTHONPATH=%~dp0cli;%PYTHONPATH%"
if exist "%~dp0runtime\python\python.exe" (
  "%~dp0runtime\python\python.exe" -m prepa_ai
  exit /b %errorlevel%
)
where py >nul 2>nul
if not errorlevel 1 (
  py -3 -m prepa_ai
  exit /b %errorlevel%
)
where python >nul 2>nul
if not errorlevel 1 (
  python -m prepa_ai
  exit /b %errorlevel%
)
echo No se encontro Python.
echo Se necesita el runtime portable en runtime\python\ o Python 3.10+ instalado.
exit /b 1
