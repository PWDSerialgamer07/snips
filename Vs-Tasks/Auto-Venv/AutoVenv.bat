@ECHO OFF
REM This script detects Python files and checks for or creates a virtual environment in the current directory.

setlocal enabledelayedexpansion

REM Check if there are any Python files in the current directory or subdirectories
set "python_files_found=false"
for /r %%F in (*.py) do (
    set "python_files_found=true"
    goto :found_python
)

:found_python
if "!python_files_found!"=="false" (
    echo No Python files found in the directory or subdirectories.
    exit /b
) else (
    echo Python files found in the directory or subdirectories.
)

REM Check if a virtual environment already exists (only if it's called .venv)
echo Checking for existing virtual environment...
if exist ".venv\Scripts\activate.bat" (
    echo Virtual environment already exists.
) else (
    echo Virtual environment not found. Creating one...
    python -m venv .venv
    echo Virtual environment created.
)

endlocal
exit /b
