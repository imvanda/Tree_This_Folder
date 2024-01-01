@echo off
Net session >nul 2>&1 || powershell start-process add_treetree.bat -verb runas
SETLOCAL EnableExtensions
: 构建安装目录
md "C:\Program Files\Tree This Folder"
:: 复制文件到安装目录
copy "%~dp0treetree.ico" "C:\Program Files\Tree This Folder\treetree.ico"
copy "%~dp0treetree.bat" "C:\Program Files\Tree This Folder\treetree.bat"
copy "%~dp0remove_treetree.bat" "C:\Program Files\Tree This Folder\remove_treetree.bat"
:: 在文件夹背景中添加右键菜单项
reg import "%~dp0treetree.reg"

echo 右键菜单项已添加。
pause
ENDLOCAL
