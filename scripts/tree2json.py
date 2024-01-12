import os
import json
import base64
import mimetypes
import zlib
import pyperclip

from configparser import ConfigParser
config = ConfigParser()

main_path = "C:\\Program Files\\Tree This Folder"
config_file_path = os.path.join(main_path, "config.ini")
treeignore_file_path = os.path.join(main_path, ".treeignore")

def read_file_content(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type and mime_type.startswith("text"):
        with open(file_path, "r", errors='ignore') as f:
            content = f.read()
    else:
        with open(file_path, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf-8")
    return content

def compress_content(content):
    return base64.b64encode(zlib.compress(content.encode("utf-8"))).decode("utf-8")

def decompress_content(content):
    return zlib.decompress(base64.b64decode(content.encode("utf-8"))).decode("utf-8")

def generate_tree(path, level_limit=None, current_level=0):
    if not os.path.exists(path) or (level_limit is not None and current_level > level_limit):
        return None

    tree = {"type": "directory", "name": os.path.basename(path), "children": []}

    for element in sorted(os.listdir(path)):
        element_path = os.path.join(path, element)

        if os.path.isdir(element_path):
            tree["children"].append(generate_tree(element_path, level_limit, current_level + 1))
        else:
            tree["children"].append({
                "type": "file",
                "name": element,
                "content": compress_content(read_file_content(element_path))
            })

    return tree

def save_tree_json(tree, output_file_name):
    with open(output_file_name, "w", encoding='utf-8') as f:
        json.dump(tree, f, indent=2)

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
    folder_path = os.getcwd()
    global level_limit
    level_limit = 20
    read_level_limit()

    output_file_name = os.path.split(folder_path)[-1] + ".json"
    tree = generate_tree(folder_path, level_limit)
    print(f"Json文件 {output_file_name} 已生成。")
    save_tree_json(tree, output_file_name)
    copy_txt_to_clipboard(output_file_name)

if __name__ == "__main__":
    main()