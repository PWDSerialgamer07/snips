@ECHO OFF
REM This script's goal is to detect if there are Python files, check for virtual environments, and create one if necessary.
REM It will run within the directory opened in VSCode (${workspaceFolder}).

set "python_files_found=false"
setlocal enabledelayedexpansion

REM Check if the folder path was provided (from VSCode workspace)
if "%1"=="" (
    echo No directory provided. Usage: auto_venv.bat [directory]
    exit /b
)

set "target_dir=%1"

REM Check if the directory exists
if not exist "%target_dir%" (
    echo The directory "%target_dir%" does not exist
    exit /b
)

REM Move to the target directory
cd /d "%target_dir%"

REM Check if there are any Python files in the directory or subdirectories
for /r %%F in (*.py) do (
    set "python_files_found=true"
)

REM Confirm if no Python files are found
if "!python_files_found!"=="false" (
    echo No Python files found in the directory or subdirectories.
    exit /b
) else (
    echo Python files found in the directory or subdirectories.
)

REM Check if a virtual environment already exists
echo Checking for existing virtual environment...
if exist "venv\Scripts\activate.bat" (
    echo Virtual environment already exists.
) else (
    echo Virtual environment not found. Creating one...
    python -m venv .venv
    Rem Should be python3, but my python install is very messed up soooo...
    echo Virtual environment created.
)

:: End of script
endlocal
exit /b
