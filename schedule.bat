@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
set "TASK_NAME=CodexDailyDigest"
set "PYTHON=python"

echo ============================================
echo   Daily Digest - Task Scheduler Manager
echo ============================================
echo.
echo 1. Register daily task (9:00 AM)
echo 2. Unregister task
echo 3. Run once now
echo 4. Show task status
echo 5. Open Dashboard
echo 6. Exit
echo.

choice /c 123456 /n /m "Choose (1-6): "
if errorlevel 6 exit /b
if errorlevel 5 goto dashboard
if errorlevel 4 goto status
if errorlevel 3 goto runnow
if errorlevel 2 goto unregister
if errorlevel 1 goto register

:register
echo.
echo [*] Registering scheduled task...
schtasks /create /tn "%TASK_NAME%" /tr "'%PYTHON%' '%SCRIPT_DIR%digest.py' --no-open" /sc daily /st 09:00 /f
if %errorlevel% equ 0 (
    echo [OK] Task registered: runs daily at 9:00 AM
) else (
    echo [x] Failed. Try running as Administrator.
)
goto end

:unregister
echo.
echo [*] Unregistering task...
schtasks /delete /tn "%TASK_NAME%" /f
echo [OK] Task removed.
goto end

:runnow
echo.
echo [*] Running digest generation...
cd /d "%SCRIPT_DIR%"
"%PYTHON%" digest.py --no-open
goto end

:dashboard
echo.
echo [*] Starting dashboard...
cd /d "%SCRIPT_DIR%"
start http://127.0.0.1:8080
"%PYTHON%" digest.py --serve
goto end

:status
echo.
echo [*] Task status:
schtasks /query /tn "%TASK_NAME%" /fo LIST /v 2>nul || echo [x] Task not found.
goto end

:end
echo.
pause
