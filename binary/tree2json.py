import os
import json
import base64
import mimetypes
import zlib
import pyperclip

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

def generate_tree(path):
    if not os.path.exists(path):
        return None

    tree = {"type": "directory", "name": os.path.basename(path), "children": []}

    for element in sorted(os.listdir(path)):
        element_path = os.path.join(path, element)

        if os.path.isdir(element_path):
            tree["children"].append(generate_tree(element_path))
        else:
            tree["children"].append({
                "type": "file",
                "name": element,
                "content": compress_content(read_file_content(element_path))
            })

    return tree

def save_tree_json(tree, output_file):
    with open(output_file, "w", encoding='utf-8') as f:
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

if __name__ == "__main__":
    folder_path = os.getcwd()
    output_file = os.path.split(folder_path)[-1] + ".json"
    tree = generate_tree(folder_path)
    print(f"Json文件 {output_file} 已生成。")
    save_tree_json(tree, output_file)
    copy_txt_to_clipboard(output_file)