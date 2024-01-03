# -*- coding: utf-8 -*-
import ctypes
import os
import subprocess

def is_admin():
    """检查用户是否具有管理员权限"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def run_as_admin(command):
    "需要vac"
    subprocess.run(["powershell", "Start-Process", command, "-Verb", "RunAs"], shell=True)


def main():
    if not is_admin():
        print("错误：此程序需要以管理员权限运行。请以管理员身份重启程序。")
        input("按任意键退出...")
        return
    while True:
        # 显示菜单
        print("---------------------")
        print("1. 添加 复制文件夹结构")
        print("2. 添加 生成文件夹结构")
        print("3. 移除 复制文件夹结构")
        print("4. 移除 生成文件夹结构")
        print("0. 退出")
        print("---------------------")

        choice = input("请输入选项并按Enter键: ")

        if choice == "0":
            print("退出循环")
            break
        elif choice == "1":
            run_as_admin("..\\复制文件夹结构\\add_treejustcopy.bat")
        elif choice == "2":
            run_as_admin("..\\生成文件夹结构\\add_treegenerate.bat")
        elif choice == "3":
            run_as_admin("..\\复制文件夹结构\\remove_treejustcopy.bat")
        elif choice == "4":
            run_as_admin("..\\生成文件夹结构\\remove_treegenerate.bat")
        else:
            print("无效的选项，请重新输入。")

        input("按任意键继续...")
        os.system('cls')  # 清除屏幕


if __name__ == "__main__":
    main()
