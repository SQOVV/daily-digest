@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo [*] Starting dashboard at http://127.0.0.1:8080
echo [*] Press Ctrl+C to stop
echo.
start http://127.0.0.1:8080
python digest.py --serve
pause
