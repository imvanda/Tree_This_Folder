# -*- coding: utf-8 -*-

import os
import sys
import hashlib
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

def clean_identifier(identifier):
    """Replace special characters with underscores in identifier."""
    return identifier.replace('.', '_').replace(os.sep, '_').replace('-', '_').replace(' ', '_')


def generate_plantuml_content(base_path, current_path, level, level_limit):
    """Recursively generate PlantUML content from directory structure."""
    matches_gitignore = parse_gitignore(local_treeignore_file_path)
    content_list = []
    dirs = sorted(os.listdir(current_path))

    for name in dirs:
        if name.startswith('.'):
            continue

        sub_path = os.path.join(current_path, name)
        relative_path = os.path.relpath(sub_path, base_path)
        identifier = clean_identifier(relative_path)

        if os.path.isdir(sub_path) and level < level_limit:
            # Check if the file matches any pattern in .gitignore
            if not matches_gitignore(name):
                content_list.append(f'package "{name}" as {identifier} {{\n')
                content_list += generate_plantuml_content(base_path, sub_path, level + 1, level_limit)
                content_list.append('}\n')

                if current_path != base_path:
                    parent_identifier = clean_identifier(os.path.relpath(current_path, base_path))
                    content_list.append(f"{parent_identifier} -- {identifier}\n")
            else:
                print("Skipping:", sub_path + "\n")
                continue

    return content_list


def calculate_content_hash(content):
    """Calculate and return the MD5 hash of the content."""
    return hashlib.md5(content.encode('utf-8')).hexdigest()[:6]


def read_level_limit():
    if os.path.exists(config_file_path):
        global level_limit
        config.read(config_file_path)
        level_limit = int(config['DEFAULT']['level_limit'])


def main():
    # 获取当前文件夹路径和设置探索层级深度
    base_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    global level_limit
    level_limit = 20
    read_level_limit()

    # 设置初始层级，level = 0 探索层级深度为0时仅输出当前文件夹，不向下探索，我们取巧直接level_limit+1实现同样效果
    level = 0
    plantuml_content = ["@startuml\n", "scale 103500 width\n", "scale 2200 height\n"]
    plantuml_content += generate_plantuml_content(base_path, base_path, level, level_limit+1)
    plantuml_content.append("@enduml\n")
    content_str = ''.join(plantuml_content)
    content_hash = calculate_content_hash(content_str)
    
    # 设置输出文件名
    output_file_name = os.path.join(base_path, os.path.basename(os.path.normpath(base_path)) + '_' + content_hash + '.puml')
    if not os.path.exists(local_treeignore_file_path):
        create_local_treeignore_file()


    print(f"Generating PlantUML file at: {output_file_name}")

    with open(output_file_name, 'w', encoding='utf-8') as plantuml_file:
        plantuml_file.write(content_str)

    print(f"PlantUML file has been generated at: {output_file_name}")

    try:
        pyperclip.copy(content_str)
        print("The file content has been copied to the clipboard.")
    except Exception as e:
        print(f"An error occurred while copying to the clipboard: {e}")


if __name__ == "__main__":
    main()