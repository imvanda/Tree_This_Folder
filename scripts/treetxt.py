import os
import pyperclip
from gitignore_parser import parse_gitignore
from configparser import ConfigParser
config = ConfigParser()

main_path = "C:\\Program Files\\Tree This Folder"
config_file_path = os.path.join(main_path, "config.ini")
treeignore_file_path = os.path.join(main_path, ".treeignore")
local_treeignore_file_path = os.path.join(os.getcwd(), ".treeignore")


def create_local_treeignore_file():
    # 读取源文件内容
    try:
        with open(treeignore_file_path, 'r') as source_file:
            content_to_add = source_file.read()

        # 写入内容到新文件
        with open(local_treeignore_file_path, 'a') as new_file:
            new_file.write('\n' + content_to_add)

        print(f'文件 {treeignore_file_path} 的内容已成功写入到 {local_treeignore_file_path}')
    except FileNotFoundError:
        print(f'找不到文件 {treeignore_file_path}')
    except Exception as e:
        print(f'发生错误: {e}')


def list_files_recursively(start_path, output_file, level, level_limit):
    matches_gitignore = parse_gitignore(local_treeignore_file_path)
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(start_path):
            current_level = root[len(start_path):].count(os.sep) + level
            print(f"Level: {current_level}")
            if current_level > level_limit:
                del dirs[:]
                continue

            # Check if the root matches any pattern in .gitignore
            if matches_gitignore(os.path.relpath(root, start_path)):
                print("Skipping:", root)
                del dirs[:]
                continue

            for file_or_dir in files + dirs:
                abs_path = os.path.abspath(os.path.join(root, file_or_dir))

                # Check if the file matches any pattern in .gitignore
                if not matches_gitignore(os.path.relpath(abs_path, start_path)):
                    f.write(abs_path + '\n')
                else:
                    print("Skipping:", abs_path)
                    continue


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
    path = os.getcwd()
    global level_limit
    level_limit = 20
    read_level_limit()
    # 设置初始层级和输出文件名，level = 0 探索层级深度为0时仅输出当前文件夹，不向下探索
    level = 0
    output_file_name = 'Folder_Structure.txt'
    if not os.path.exists(local_treeignore_file_path):
        create_local_treeignore_file()

    list_files_recursively(path, output_file_name, level, level_limit)
    copy_txt_to_clipboard(output_file_name)

if __name__ == '__main__':
    main()
