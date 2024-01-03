@echo off
Net session >nul 2>&1 || powershell start-process add_treejustcopy.bat -verb runas
SETLOCAL EnableExtensions
: 构建安装目录
md "C:\Program Files\Tree This Folder"
:: 复制文件到安装目录
copy "%~dp0treejustcopy.ico" "C:\Program Files\Tree This Folder\treejustcopy.ico"
copy "%~dp0treejustcopy.bat" "C:\Program Files\Tree This Folder\treejustcopy.bat"
copy "%~dp0remove_treejustcopy.bat" "C:\Program Files\Tree This Folder\remove_treejustcopy.bat"
:: 在文件夹背景中添加右键菜单项
reg import "%~dp0treejustcopy.reg"

echo 右键菜单项已添加。
pause
ENDLOCAL
