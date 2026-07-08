@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo 启动机动车交通事故赔偿评估系统...
echo.
python app.py
pause
