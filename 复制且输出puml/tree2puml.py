# -*- coding: utf-8 -*-

import os
import sys
import hashlib
import pyperclip

def has_single_subdir(path):
    """Check if a directory contains only a single subdirectory."""
    items = os.listdir(path)
    if len(items) == 1 and os.path.isdir(os.path.join(path, items[0])):
        return items[0]
    return None
def clean_identifier(identifier):
    """Replace special characters with underscores in identifier."""
    return identifier.replace('.', '_').replace(os.sep, '_').replace('-', '_').replace(' ', '_')


def generate_plantuml_content(base_path, current_path, level, level_limit):
    """Recursively generate PlantUML content from directory structure."""
    content_list = []
    dirs = sorted(os.listdir(current_path))

    for name in dirs:
        if name.startswith('.'):
            continue

        sub_path = os.path.join(current_path, name)

        if os.path.isdir(sub_path):
            single_subdir = has_single_subdir(sub_path)
            if single_subdir:
                sub_path = os.path.join(sub_path, single_subdir)
                name = os.path.join(name, single_subdir)


        relative_path = os.path.relpath(sub_path, base_path)
        identifier = clean_identifier(relative_path)

        if os.path.isdir(sub_path) and level < level_limit:
            content_list.append(f'package "{name}" as {identifier} {{\n')
            content_list += generate_plantuml_content(base_path, sub_path, level + 1, level_limit)
            content_list.append('}\n')

            if current_path != base_path:
                parent_identifier = clean_identifier(os.path.relpath(current_path, base_path))
                content_list.append(f"{parent_identifier} -- {identifier}\n")

    return content_list


def calculate_content_hash(content):
    """Calculate and return the MD5 hash of the content."""
    return hashlib.md5(content.encode('utf-8')).hexdigest()[:6]


def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    plantuml_content = ["@startuml\n", "scale 103500 width\n", "scale 2200 height\n"]
    plantuml_content += generate_plantuml_content(base_path, base_path, 0, 20)
    plantuml_content.append("@enduml\n")
    content_str = ''.join(plantuml_content)
    content_hash = calculate_content_hash(content_str)

    output_file_name = os.path.join(base_path,
                                    os.path.basename(os.path.normpath(base_path)) + '_' + content_hash + '.puml')
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
