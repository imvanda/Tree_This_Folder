@echo off
Net session >nul 2>&1 || powershell start-process remove_treegenerate.bat -verb runas
SETLOCAL EnableExtensions

:: 删除之前在文件夹背景中添加的注册表项
REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\Item0" /f
REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\Item1" /f
REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\Item2" /f
REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\Item3" /f
REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\Item4" /f
REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\Item5" /f
REG DELETE "HKEY_CLASSES_ROOT\Directory\Background\shell\Item0" /f
:: 延时
ping 127.0.0.1 -n 2 >nul
echo 右键菜单项已删除。
: 删除安装文件
del /s /q "C:\Program Files\Tree This Folder\TreeThisFolder.ico"

del /s /q "C:\Program Files\Tree This Folder\treetxt.bat"
del /s /q "C:\Program Files\Tree This Folder\treemd.bat"
del /s /q "C:\Program Files\Tree This Folder\tree2puml.bat"
del /s /q "C:\Program Files\Tree This Folder\treetree.bat"
del /s /q "C:\Program Files\Tree This Folder\treeseedir.bat"
del /s /q "C:\Program Files\Tree This Folder\tree2json.bat"

del /s /q "C:\Program Files\Tree This Folder\treemd.exe"
del /s /q "C:\Program Files\Tree This Folder\tree2puml.exe"
del /s /q "C:\Program Files\Tree This Folder\treeseedir.exe"
del /s /q "C:\Program Files\Tree This Folder\tree2json.exe"

del /s /q "C:\Program Files\Tree This Folder\treemd.py"
del /s /q "C:\Program Files\Tree This Folder\tree2puml.py"
del /s /q "C:\Program Files\Tree This Folder\treeseedir.py"
del /s /q "C:\Program Files\Tree This Folder\tree2json.py"

rd /s /q "C:\Program Files\Tree This Folder\runtime"

rd /s /q "C:\Program Files\Tree This Folder\site-packages"

del /s /q "C:\Program Files\Tree This Folder\remove_treegenerate.bat"
pause
ENDLOCAL