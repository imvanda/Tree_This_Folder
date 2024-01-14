import os
import pyperclip
import seedir

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

def my_style(item):
    outdict = {}
    # get the extension
    ext = os.path.splitext(item)[1]
    file_types = {
        'text': ('.txt', '.md', '.json', '.log', '.ini', '.cfg'),
        'image': ('.png', '.jpg', '.gif', '.bmp', '.tif', '.svg', '.eps', '.psd', '.tiff', '.raw', '.indd', '.ai', '.xcf', '.sketch', '.skp', '.jpeg', '.jfif', '.exif', '.cr2', '.svgz', '.ico', '.jng', '.bmp', '.ps', '.pnm', '.pcx', '.djvu', '.webp', '.tga', '.svgz'),
        'audio': ('.mp3', '.aac', '.ogg', '.wma', '.m4a', '.midi', '.opus', '.flac', '.wav', '.ape', '.alac', '.wv', '.aa', '.m4p', '.au', '.aiff', '.ra', '.snd', '.amr', '.aacp', '.mka', '.dsd', '.gsm', '.iklax', '.it', '.kar', '.m3u', '.m3u8', '.m4b', '.mid', '.mod', '.msv', '.oga'),
        'video': ('.avi', '.mov', '.wmv', '.mp4', '.mkv', '.flv', '.3gp', '.webm', '.rm', '.swf', '.vob', '.ogv', '.drc', '.gifv', '.mng', '.qt', '.yuv', '.rmvb', '.asf', '.m4v', '.m2v', '.svi', '.f4v', '.vob'),
        'archive': ('.rar', '.zip', '.tar', '.gz', '.7z', '.pkg', '.deb', '.rpm', '.arj', '.z', '.iso', '.lz', '.lzh', '.lzma', '.cab', '.chm', '.wim', '.dmg', '.efi', '.img', '.egg', '.alz', '.s7z', '.sitx', '.xz'),
        'document': ('.doc', '.docx', '.docm', '.dot', '.dotx', '.dotm', '.odf', '.rtf', '.wpd', '.msg', '.eml', '.pst', '.ost', '.mbox', '.emlx', '.mht', '.mhtml', '.html', '.xps', '.oxps', '.pdf' '.odt', '.yaml', '.xml', '.tex', '.yml', '.sql', '.java', '.py', '.c', '.cpp', '.h', '.hpp', '.js', '.css', '.php', '.rb', '.pl', '.asm'),
        'executable': ('.exe', '.dll', '.com', '.bat', '.cmd', '.msi', '.app', '.vb', '.vbs', '.vbe', '.js', '.jse', '.wsf', '.wsh', '.ps1', '.psm1', '.psd1', '.psc1', '.pssc', '.sh', '.bash', '.csh', '.tcsh', '.ksh', '.zsh'),
        'spreadsheet': ('.csv', '.tsv', '.xls', '.xlsx', '.xlsm', '.xltx', '.xltm', '.xlsb', '.xlam', '.ods', '.prn', '.dif', '.sdc', '.dbf'),
        'presentation': ('.ppt', '.pptx', '.pot', '.potx', '.potm', '.pps', '.ppsx', '.ppsm', '.odp'),
        'miscellaneous': ('.nfo', '.inf')
    }

    file_emojis = {
        'text': '✏️',
        'image': '🖼️',
        'audio': '🎵',
        'video': '🎥',
        'archive': '🗃️',
        'document': '📜',
        'executable': '🛠️',
        'spreadsheet': '📊',
        'presentation': '📽️',
        'miscellaneous': '📃'
    }

    file_type = None

    for file_category, extensions in file_types.items():
        if ext in extensions:
            file_type = file_category
            break

    if file_type:
        outdict['filestart'] = file_emojis[file_type]
    else:
        outdict['filestart'] = '📄'  # Default emoji for unknown file type


    file_type = None

    for file_category, extensions in file_types.items():
        if ext in extensions:
            file_type = file_category
            break

    if file_type:
        outdict['filestart'] = file_emojis[file_type]
    else:
        outdict['filestart'] = '📄'  # Default emoji for unknown file type


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

def read_level_limit():
    if os.path.exists(config_file_path):
        global level_limit
        config.read(config_file_path)
        level_limit = int(config['DEFAULT']['level_limit'])

def read_gitignore(file_path):
    exclude_folders = []
    exclude_files = []

    with open(file_path, 'r') as file:
        for line in file:
            # 忽略注释和空行
            if line.strip() and not line.strip().startswith('#'):
                item = line.strip()
                if item.endswith('/'):
                    # 如果以斜杠结尾，则为文件夹
                    exclude_folders.append(item.lstrip('/').rstrip('/'))
                else:
                    # 否则为文件
                    exclude_files.append(item.lstrip('/'))

    return exclude_folders, exclude_files

def main():
    # 获取当前文件夹路径和设置探索层级深度
    path = os.getcwd()
    global level_limit
    level_limit = 20
    read_level_limit()

    # 设置初始层级和输出文件名 seedir未提供设置初始层级接口，level = 1 探索层级深度为0时仅输出当前文件夹，不向下探索，我们取巧直接depthlimit=level_limit+level实现同样效果
    level = 1
    output_file_name = os.path.split(path)[-1] + '_seedir.txt'
    if not os.path.exists(local_treeignore_file_path):
        create_local_treeignore_file()

    exclude_folders, exclude_files = read_gitignore(local_treeignore_file_path)
    print("排除的文件夹：", exclude_folders)
    print("排除的文件：", exclude_files)
    content_str = seedir.seedir(path, style='emoji', printout=False, formatter=my_style, sticky_formatter=True, exclude_folders=exclude_folders, exclude_files=exclude_files, depthlimit=level_limit+level)
    # 打开Txt文件并开始分析目录结构
    with open(output_file_name, 'w', encoding='utf-8') as seedir_file:
        seedir_file.write(content_str)
    print(f"seedir文件 {output_file_name} 已生成。")
    copy_txt_to_clipboard(output_file_name)


if __name__ == "__main__":
    main()