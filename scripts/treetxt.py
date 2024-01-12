import os
import pyperclip

from configparser import ConfigParser
config = ConfigParser()

main_path = "C:\\Program Files\\Tree This Folder"
config_file_path = os.path.join(main_path, "config.ini")
treeignore_file_path = os.path.join(main_path, ".treeignore")

def list_files_recursively(start_path, output_file, level_limit=None):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(start_path):
            current_level = root[len(start_path):].count(os.sep)  # 计算当前层级

            # 检查是否达到层级限制
            if level_limit is not None and current_level >= level_limit:
                del dirs[:]  # 清空dirs以阻止os.walk进入下一级子目录
                continue

            for file_or_dir in files + dirs:
                abs_path = os.path.abspath(os.path.join(root, file_or_dir))
                f.write(abs_path + '\n')

def copy_txt_to_clipboard(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            pyperclip.copy(content)
            print("文件内容已复制到剪贴板")
    except FileNotFoundError:
        print(f"找不到文件：{file_path}")
    except Exception as e:
        print(f"发生错误：{e}")

def read_level_limit():
    if os.path.exists(config_file_path):
        global level_limit
        config.read(config_file_path)
        level_limit = int(config['DEFAULT']['level_limit'])

def main():
    # 获取当前文件夹路径和设置探索层级深度
    path = os.getcwd()
    global level_limit
    level_limit = 20
    read_level_limit()

    # 设置输出文件名
    output_file_name = 'Folder_Structure.txt'

    # 打开Txt文件并开始分析目录结构
    list_files_recursively(path, output_file_name, level_limit)
    copy_txt_to_clipboard(output_file_name)

if __name__ == '__main__':
    main()