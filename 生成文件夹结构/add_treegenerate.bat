@echo off
Net session >nul 2>&1 || powershell start-process add_treegenerate.bat -verb runas
SETLOCAL EnableExtensions

:: ������װĿ¼
md "C:\Program Files\Tree This Folder"
:: �����ļ�����װĿ¼
copy "%~dp0TreeThisFolder.ico" "C:\Program Files\Tree This Folder\TreeThisFolder.ico"

copy "%~dp0treetxt.bat" "C:\Program Files\Tree This Folder\treetxt.bat"
copy "%~dp0treemd.bat" "C:\Program Files\Tree This Folder\treemd.bat"
copy "%~dp0tree2puml.bat" "C:\Program Files\Tree This Folder\tree2puml.bat"
copy "%~dp0treetree.bat" "C:\Program Files\Tree This Folder\treetree.bat"
copy "%~dp0treeseedir.bat" "C:\Program Files\Tree This Folder\treeseedir.bat"
copy "%~dp0tree2json.bat" "C:\Program Files\Tree This Folder\tree2json.bat"

copy "%~dp0..\binary\PyStand.exe" "C:\Program Files\Tree This Folder\treemd.exe"
copy "%~dp0..\binary\PyStand.exe" "C:\Program Files\Tree This Folder\tree2puml.exe"
copy "%~dp0..\binary\PyStand.exe" "C:\Program Files\Tree This Folder\treeseedir.exe"
copy "%~dp0..\binary\PyStand.exe" "C:\Program Files\Tree This Folder\tree2json.exe"

copy "%~dp0..\binary\treemd.py" "C:\Program Files\Tree This Folder\treemd.py"
copy "%~dp0..\binary\tree2puml.py" "C:\Program Files\Tree This Folder\tree2puml.py"
copy "%~dp0..\binary\treeseedir.py" "C:\Program Files\Tree This Folder\treeseedir.py"
copy "%~dp0..\binary\tree2json.py" "C:\Program Files\Tree This Folder\tree2json.py"

md "C:\Program Files\Tree This Folder\runtime"
xcopy /s /e /y "%~dp0..\runtime\" "C:\Program Files\Tree This Folder\runtime\"

md "C:\Program Files\Tree This Folder\site-packages"
xcopy /s /e /y "%~dp0..\site-packages\emoji\" "C:\Program Files\Tree This Folder\site-packages\emoji\"
xcopy /s /e /y "%~dp0..\site-packages\natsort\" "C:\Program Files\Tree This Folder\site-packages\natsort\"
xcopy /s /e /y "%~dp0..\site-packages\pyperclip\" "C:\Program Files\Tree This Folder\site-packages\pyperclip\"
:: xcopy /s /e /y "%~dp0..\site-packages\PyQt6\" "C:\Program Files\Tree This Folder\site-packages\PyQt6\"    ����ҪPyQt6
xcopy /s /e /y "%~dp0..\site-packages\seedir\" "C:\Program Files\Tree This Folder\site-packages\seedir\"


copy "%~dp0remove_treegenerate.bat" "C:\Program Files\Tree This Folder\remove_treegenerate.bat"
:: ���ļ��б���������Ҽ��˵���
reg import "%~dp0treegenerate.reg"
echo �Ҽ��˵�������ӡ�
pause
ENDLOCAL
