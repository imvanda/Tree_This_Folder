@echo off
Net session >nul 2>&1 || powershell start-process add_treegenerate.bat -verb runas
SETLOCAL EnableExtensions

:: 构建安装目录
md "C:\Program Files\Tree This Folder"
:: 复制文件到安装目录
copy "%~dp0TreeThisFolder.ico" "C:\Program Files\Tree This Folder\TreeThisFolder.ico"

copy "%~dp0treetxt.bat" "C:\Program Files\Tree This Folder\treetxt.bat"
copy "%~dp0treemd.bat" "C:\Program Files\Tree This Folder\treemd.bat"
copy "%~dp0tree2puml.bat" "C:\Program Files\Tree This Folder\tree2puml.bat"
copy "%~dp0treetree.bat" "C:\Program Files\Tree This Folder\treetree.bat"
copy "%~dp0treeseedir.bat" "C:\Program Files\Tree This Folder\treeseedir.bat"

copy "%~dp0..\binary\PyStand.exe" "C:\Program Files\Tree This Folder\treemd.exe"
copy "%~dp0..\binary\PyStand.exe" "C:\Program Files\Tree This Folder\tree2puml.exe"
copy "%~dp0..\binary\PyStand.exe" "C:\Program Files\Tree This Folder\treeseedir.exe"

copy "%~dp0..\binary\treemd.py" "C:\Program Files\Tree This Folder\treemd.py"
copy "%~dp0..\binary\tree2puml.py" "C:\Program Files\Tree This Folder\tree2puml.py"
copy "%~dp0..\binary\treeseedir.py" "C:\Program Files\Tree This Folder\treeseedir.py"

md "C:\Program Files\Tree This Folder\runtime"
xcopy /s /e /y "%~dp0..\runtime\" "C:\Program Files\Tree This Folder\runtime\"

md "C:\Program Files\Tree This Folder\site-packages"
xcopy /s /e /y "%~dp0..\site-packages\emoji\" "C:\Program Files\Tree This Folder\site-packages\emoji\"
xcopy /s /e /y "%~dp0..\site-packages\natsort\" "C:\Program Files\Tree This Folder\site-packages\natsort\"
xcopy /s /e /y "%~dp0..\site-packages\pyperclip\" "C:\Program Files\Tree This Folder\site-packages\pyperclip\"
@REM xcopy /s /e /y "%~dp0..\site-packages\PyQt6\" "C:\Program Files\Tree This Folder\site-packages\PyQt6\"    不需要PyQt6
xcopy /s /e /y "%~dp0..\site-packages\seedir\" "C:\Program Files\Tree This Folder\site-packages\seedir\"


copy "%~dp0remove_treegenerate.bat" "C:\Program Files\Tree This Folder\remove_treegenerate.bat"
:: 在文件夹背景中添加右键菜单项
reg import "%~dp0treegenerate.reg"
echo 右键菜单项已添加。
pause
ENDLOCAL
