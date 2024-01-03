import os
import pyperclip
import seedir

def my_style(item):
    outdict = {}
    # get the extension
    ext = os.path.splitext(item)[1]
    if ext in ('.txt', '.md', '.doc'):
        outdict['filestart'] = '✏️'
    elif ext in ('.png', '.jpg', '.gif'):
        outdict['filestart'] = '🖼️'
    elif ext == '.mp3':
        outdict['filestart'] = '🎵'
    else:
    # 如果都不匹配的情况
        outdict['filestart'] = '📄'

    parent = os.path.basename(os.path.dirname(item))
    if parent == 'assets':
        outdict['folderstart'] = '🅰️ '
    return outdict


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


def main():
    # 获取当前文件夹路径和设置探索层级深度
    path = os.getcwd()
    level_limit = 20

    # 设置输出文件名
    file_name = os.path.split(path)[-1] + '_seedir.txt'

    content_str = seedir.seedir(path, style='emoji', printout=False, formatter=my_style, sticky_formatter=True, exclude_folders=['.git','.history'], depthlimit=level_limit)
    # 打开Txt文件并开始分析目录结构
    with open(file_name, 'w', encoding='utf-8') as seedir_file:
        seedir_file.write(content_str)
    print(f"seedir文件 {file_name} 已生成。")
    txt_file_path = file_name
    copy_txt_to_clipboard(txt_file_path)


if __name__ == "__main__":
    main()