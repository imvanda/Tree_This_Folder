@echo off
chcp 65001
:main
echo ---------------------
echo "1. 添加 复制文件夹结构"
echo "2. 添加 生成文件夹结构"
echo "3. 移除 复制文件夹结构"
echo "4. 移除 生成文件夹结构"
echo "0. 退出"
echo ---------------------
set choice=99
set /p choice=请输入选项并按Enter键:

if "%choice%"=="0" (
    echo 退出循环
    goto :eof
) else if "%choice%"=="1" (
    Net session >nul 2>&1 || powershell start-process 复制文件夹结构\add_treejustcopy.bat -verb runas
) else if "%choice%"=="2" (
    Net session >nul 2>&1 || powershell start-process 生成文件夹结构\add_treegenerate.bat -verb runas
) else if "%choice%"=="3" (
    Net session >nul 2>&1 || powershell start-process 复制文件夹结构\remove_treejustcopy.bat -verb runas
) else if "%choice%"=="4" (
    Net session >nul 2>&1 || powershell start-process 生成文件夹结构\remove_treegenerate.bat -verb runas
) else (
    echo .
)
cls
goto main