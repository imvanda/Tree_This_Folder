import os
import pyperclip
import seedir

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