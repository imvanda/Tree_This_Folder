@echo off
Net session >nul 2>&1 || powershell start-process add0.bat -verb runas
SETLOCAL EnableExtensions

:: 定义脚本名称
set SCRIPT_NAME=生成文件夹结构

:: 定义脚本相对路径
set SCRIPT_PATH="%~dp0main0.bat"
copy "%~dp0treemd.exe" "%APPDATA%\treemd.exe"
:: 在文件夹背景中添加右键菜单项
REG ADD "HKEY_CLASSES_ROOT\Directory\Background\shell\%SCRIPT_NAME%" /f
REG ADD "HKEY_CLASSES_ROOT\Directory\Background\shell\%SCRIPT_NAME%\command" /f /ve /t REG_SZ /d "cmd /c \"%SCRIPT_PATH%\""

echo 右键菜单项已添加。
pause
ENDLOCAL
