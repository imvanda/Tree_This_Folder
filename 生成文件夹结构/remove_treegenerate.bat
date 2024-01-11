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
:: 删除安装文件
del /s /q "C:\Program Files\Tree This Folder\TreeThisFolder.ico"

del /s /q "C:\Program Files\Tree This Folder\bats\treetxt.bat"
del /s /q "C:\Program Files\Tree This Folder\bats\treemd.bat"
del /s /q "C:\Program Files\Tree This Folder\bats\tree2puml.bat"
del /s /q "C:\Program Files\Tree This Folder\bats\treetree.bat"
del /s /q "C:\Program Files\Tree This Folder\bats\treeseedir.bat"
del /s /q "C:\Program Files\Tree This Folder\bats\tree2json.bat"
rd "C:\Program Files\Tree This Folder\bats\"
:: 不要用 rd /s /q "C:\Program Files\Tree This Folder\bats\" ，防止把 复制文件夹结构 功能破坏


rd /s /q "C:\Program Files\Tree This Folder\scripts\"

rd /s /q "C:\Program Files\Tree This Folder\runtime"


rd /s /q "C:\Program Files\Tree This Folder\site-packages"

del /s /q "C:\Program Files\Tree This Folder\remove_treegenerate.bat"
pause
ENDLOCAL