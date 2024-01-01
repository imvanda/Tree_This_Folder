@echo off
Net session >nul 2>&1 || powershell start-process add_treeMDorTXTorPUMLorTREE.bat -verb runas
SETLOCAL EnableExtensions

:: 构建安装目录
md "C:\Program Files\Tree This Folder"
:: 复制文件到安装目录
copy "%~dp0TreeThisFolder.ico" "C:\Program Files\Tree This Folder\TreeThisFolder.ico"
copy "%~dp0..\复制且输出txt\treetxt.bat" "C:\Program Files\Tree This Folder\treetxt.bat"
copy "%~dp0..\复制且输出md\treemd.bat" "C:\Program Files\Tree This Folder\treemd.bat"
copy "%~dp0..\复制且输出md\treemd.exe" "C:\Program Files\Tree This Folder\treemd.exe"
copy "%~dp0..\复制且输出puml\tree2puml.bat" "C:\Program Files\Tree This Folder\tree2puml.bat"
copy "%~dp0..\复制且输出puml\tree2puml.exe" "C:\Program Files\Tree This Folder\tree2puml.exe"
copy "%~dp0..\复制且输出tree\treetree.bat" "C:\Program Files\Tree This Folder\treetree.bat"
copy "%~dp0remove_treeMDorTXTorPUML.bat" "C:\Program Files\Tree This Folder\remove_treeMDorTXTorPUML.bat"
:: 在文件夹背景中添加右键菜单项
reg import "%~dp0生成文件夹结构_目录.reg"
reg import "%~dp0生成txt_子项.reg"
reg import "%~dp0生成md_子项.reg"
reg import "%~dp0生成plantuml_子项.reg"
reg import "%~dp0生成tree_子项.reg"
echo 右键菜单项已添加。
pause
ENDLOCAL
