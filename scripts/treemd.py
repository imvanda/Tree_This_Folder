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

def level_to_string(level):
    """
    将层级转换为对应的Markdown标题格式
    """
    if level <= 6:
        return "#" * level + " "
    else:
        return ("    " * (level - 7)) + "- "

def analyze_directory(path, level, level_limit, mind_map_markdown):
    """
    分析目录结构并生成Markdown格式的思维导图
    """
    matches_gitignore = parse_gitignore(local_treeignore_file_path)
    dirs = os.listdir(path)
    dirs.sort()
    for file in dirs:
        level_string = level_to_string(level)
        print(f"Level: {level}")
        sub_path = os.path.join(path, file)
        
        # Check if the file matches any pattern in .gitignore
        if not matches_gitignore(file):
            mind_map_markdown.write(level_string + file + "\n")
        else:
            print("Skipping:", level_string + sub_path + "\n")
            continue

        if os.path.isdir(sub_path) and level <= level_limit:
            sub_level = level + 1
            analyze_directory(sub_path, sub_level, level_limit, mind_map_markdown)

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

    # 设置初始层级和输出文件名，level = 1 探索层级深度为0时仅输出当前文件夹，不向下探索
    level = 1
    output_file_name = os.path.split(path)[-1] + '.md'
    if not os.path.exists(local_treeignore_file_path):
        create_local_treeignore_file()

    # 打开Markdown文件并开始分析目录结构
    with open(output_file_name, 'w', encoding='utf-8') as mind_map_markdown:
        analyze_directory(path, level, level_limit, mind_map_markdown)
    print(f"Markdown文件 {output_file_name} 已生成。")
    copy_txt_to_clipboard(output_file_name)

if __name__ == '__main__':
    main()