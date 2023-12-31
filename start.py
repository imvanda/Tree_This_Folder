import os
import sys
import subprocess
import tkinter as tk
from tkinter import ttk

def run_as_admin(command):
    subprocess.run(["powershell", "Start-Process", command, "-Verb", "RunAs"], shell=True)

def fun1():
    run_as_admin(os.path.join(basedir, "复制文件夹结构", "add_treejustcopy.bat"))

def fun2():
    run_as_admin(os.path.join(basedir, "生成文件夹结构", "add_treegenerate.bat"))

def fun3():
    run_as_admin(os.path.join(basedir, "复制文件夹结构", "remove_treejustcopy.bat"))

def fun4():
    run_as_admin(os.path.join(basedir, "生成文件夹结构", "remove_treegenerate.bat"))

class TreeThisFolderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tree_This_Folder")
        self.root.geometry("303x257")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Configure row and column weights to make buttons expand and center
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)



        button_width = 35  # Set the desired width for the buttons
        button_height = 10  # Set the desired height for the buttons

        # Create and define layout for each custom button style
        ttk.Style().layout("Custom.TButton1", [("Button.highlight", {"children": [("Button.border", {"children": [("Button.padding", {"children": [("Button.label", {"side": "left", "sticky": ""})]})]})]})])
        ttk.Style().layout("Custom.TButton2", [("Button.highlight", {"children": [("Button.border", {"children": [("Button.padding", {"children": [("Button.label", {"side": "left", "sticky": ""})]})]})]})])
        ttk.Style().layout("Custom.TButton3", [("Button.highlight", {"children": [("Button.border", {"children": [("Button.padding", {"children": [("Button.label", {"side": "left", "sticky": ""})]})]})]})])
        ttk.Style().layout("Custom.TButton4", [("Button.highlight", {"children": [("Button.border", {"children": [("Button.padding", {"children": [("Button.label", {"side": "left", "sticky": ""})]})]})]})])

        # Button 1 with color #635994
        ttk.Style().configure("Custom.TButton1", foreground="#635994", font=("Microsoft YaHei UI", 12))
        self.button1 = ttk.Button(self.root, text="  1.  ➕      添加 复制文件夹结构", command=fun1, width=button_width)
        self.button1.grid(row=0, column=0, pady=0, padx=1, columnspan=3, sticky="nsew")
        self.button1.configure(style="Custom.TButton1")
        self.root.bind('1', lambda event: fun1())  # Shortcut for Button 1

        # Button 2 with color #635994
        ttk.Style().configure("Custom.TButton2", foreground="#635994", font=("Microsoft YaHei UI", 12))
        self.button2 = ttk.Button(self.root, text="  2.  ➕      添加 生成文件夹结构", command=fun2, width=button_width)
        self.button2.grid(row=1, column=0, pady=0, padx=1, columnspan=3, sticky="nsew")
        self.button2.configure(style="Custom.TButton2")
        self.root.bind('2', lambda event: fun2())  # Shortcut for Button 2

        # Button 3 with color #B0B0B0
        ttk.Style().configure("Custom.TButton3", foreground="#B0B0B0", font=("Microsoft YaHei UI", 12))
        self.button3 = ttk.Button(self.root, text="  3.  🗑️ 移除 复制文件夹结构", command=fun3, width=button_width)
        self.button3.grid(row=2, column=0, pady=0, padx=1, columnspan=3, sticky="nsew")
        self.button3.configure(style="Custom.TButton3")
        self.root.bind('3', lambda event: fun3())  # Shortcut for Button 3

        # Button 4 with color #B0B0B0
        ttk.Style().configure("Custom.TButton4", foreground="#B0B0B0", font=("Microsoft YaHei UI", 12))
        self.button4 = ttk.Button(self.root, text="  4.  🗑️ 移除 生成文件夹结构", command=fun4, width=button_width)
        self.button4.grid(row=3, column=0, pady=0, padx=1, columnspan=3, sticky="nsew")
        self.button4.configure(style="Custom.TButton4")
        self.root.bind('4', lambda event: fun4())  # Shortcut for Button 4

if getattr(sys, 'frozen', None):
    basedir = sys._MEIPASS
else:
    basedir = os.path.dirname(__file__)

def main():
    root = tk.Tk()
    app = TreeThisFolderApp(root)
    root.iconbitmap(default=os.path.join(basedir, "生成文件夹结构", "TreeThisFolder.ico"))
    root.mainloop()

if __name__ == '__main__':
    main()
