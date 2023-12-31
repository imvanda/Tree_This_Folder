@echo off
Net session >nul 2>&1 || powershell start-process add0.bat -verb runas
SETLOCAL EnableExtensions

:: 定义脚本相对路径
md "C:\Program Files\Tree This Folder"
copy "%~dp0TreeThisFolder.ico" "C:\Program Files\Tree This Folder\TreeThisFolder.ico"
copy "%~dp0..\复制且输出txt\main0.bat" "C:\Program Files\Tree This Folder\treetxt.bat"
copy "%~dp0..\复制且输出md\main0.bat" "C:\Program Files\Tree This Folder\treemd.bat"
copy "%~dp0..\复制且输出md\treemd.exe" "C:\Program Files\Tree This Folder\treemd.exe"
:: 在文件夹背景中添加右键菜单项
reg import "%~dp0生成文件夹结构_目录.reg"
reg import "%~dp0生成txt_子项.reg"
reg import "%~dp0生成md_子项.reg"
echo 右键菜单项已添加。
pause
ENDLOCAL
