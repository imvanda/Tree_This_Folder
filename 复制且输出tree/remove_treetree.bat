@echo off
Net session >nul 2>&1 || powershell start-process remove_treetree.bat -verb runas
SETLOCAL EnableExtensions
:: 定义先前添加的脚本名称
set SCRIPT_NAME=生成文件夹结构
:: 删除之前在文件夹背景中添加的注册表项
REG DELETE "HKEY_CLASSES_ROOT\Directory\Background\shell\%SCRIPT_NAME%" /f
:: 延时
ping 127.0.0.1 -n 2 >nul
echo 右键菜单项已删除。
: 删除安装文件
del /s /q "C:\Program Files\Tree This Folder\treetree.ico"
del /s /q "C:\Program Files\Tree This Folder\treetree.bat"
del /s /q "C:\Program Files\Tree This Folder\remove_treetree.bat"
pause
ENDLOCAL