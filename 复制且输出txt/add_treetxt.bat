@echo off
Net session >nul 2>&1 || powershell start-process add_treetxt.bat -verb runas
SETLOCAL EnableExtensions
: 构建安装目录
md "C:\Program Files\Tree This Folder"
:: 复制文件到安装目录
copy "%~dp0treetxt.ico" "C:\Program Files\Tree This Folder\treetxt.ico"
copy "%~dp0treetxt.bat" "C:\Program Files\Tree This Folder\treetxt.bat"
copy "%~dp0remove_treetxt.bat" "C:\Program Files\Tree This Folder\remove_treetxt.bat"
:: 在文件夹背景中添加右键菜单项
reg import "%~dp0treetxt.reg"

echo 右键菜单项已添加。
pause
ENDLOCAL
