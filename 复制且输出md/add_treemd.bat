@echo off
Net session >nul 2>&1 || powershell start-process add_treemd.bat -verb runas
SETLOCAL EnableExtensions
:: 构建安装目录
md "C:\Program Files\Tree This Folder"
:: 复制文件到安装目录
copy "%~dp0treemd.ico" "C:\Program Files\Tree This Folder\treemd.ico"
copy "%~dp0treemd.bat" "C:\Program Files\Tree This Folder\treemd.bat"
copy "%~dp0treemd.exe" "C:\Program Files\Tree This Folder\treemd.exe"
copy "%~dp0remove_treemd.bat" "C:\Program Files\Tree This Folder\remove_treemd.bat"
:: 在文件夹背景中添加右键菜单项
reg import "%~dp0treemd.reg"

echo 右键菜单项已添加。
pause
ENDLOCAL
