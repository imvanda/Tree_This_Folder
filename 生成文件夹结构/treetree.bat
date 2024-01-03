@echo off
cd %V
tree /F > tree.txt
type tree.txt | clip