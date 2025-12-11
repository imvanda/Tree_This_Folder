import os
from gitignore_parser import parse_gitignore

main_path = "C:\\Program Files\\Tree This Folder"
config_file_path = os.path.join(main_path, "config.ini")
treeignore_file_path = os.path.join(main_path, ".treeignore")

matches = parse_gitignore(treeignore_file_path)
print (matches(os.path.join(main_path, "main.py")))
print (matches(os.path.join(main_path, ".treeignore")))