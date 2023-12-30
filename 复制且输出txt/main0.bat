@echo off
cd %V
dir /s /b > Folder_Structure.txt
type Folder_Structure.txt | clip