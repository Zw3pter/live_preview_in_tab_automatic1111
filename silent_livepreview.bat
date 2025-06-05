@echo off
echo Launching silent preview server...
start "" python "%~dp0silent_server.py"
timeout /t 1 >nul
start http://localhost:7861/live_preview.html
