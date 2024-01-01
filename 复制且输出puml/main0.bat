SETLOCAL EnableExtensions

echo Running script with debugging information...

echo Current directory: %CD%

if "%V%" == "" (
    echo %V% is not set, staying in the current directory.
) else (
    echo Changing directory to: %V
    cd %V
)

echo Starting tree2puml.exe from Program Files...
start "" "C:\Program Files\Tree This Folder\tree2puml.exe"
