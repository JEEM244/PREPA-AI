@echo off
setlocal
cd /d "%~dp0"
if exist "%~dp0PREPA-AI.exe" (
  "%~dp0PREPA-AI.exe" %*
  exit /b %errorlevel%
)
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
echo Usa PREPA-AI.exe o coloca Python portable en runtime\python\.
exit /b 1
