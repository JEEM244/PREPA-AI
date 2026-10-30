@echo off
setlocal
cd /d "%~dp0"
if exist "%~dp0runtime\python\python.exe" (
  "%~dp0runtime\python\python.exe" "%~dp0cli\prepa_ai.py" %*
  exit /b %errorlevel%
)
where py >nul 2>nul
if not errorlevel 1 (
  py -3 "%~dp0cli\prepa_ai.py" %*
  exit /b %errorlevel%
)
where python >nul 2>nul
if not errorlevel 1 (
  python "%~dp0cli\prepa_ai.py" %*
  exit /b %errorlevel%
)
echo No se encontro Python. El runtime portable se agregara en una siguiente etapa.
echo Coloca python.exe en runtime\python\ o usa un equipo con Python 3.10 o superior.
exit /b 1
