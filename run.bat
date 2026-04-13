@echo off
REM First Standard Bank - Launcher Script for Windows

cls
echo.
echo ╔══════════════════════════════════════════════╗
echo ║     🏦 First Standard Bank Application      ║
echo ╚══════════════════════════════════════════════╝
echo.
echo Select which interface you want to run:
echo.
echo 1) Console Demo     - Quick demonstration
echo 2) Web App         - Browser-based interface
echo 3) Desktop GUI     - Windows desktop application
echo 4) Exit
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    cls
    echo.
    echo Starting Console Demo...
    echo.
    python main.py
    pause
) else if "%choice%"=="2" (
    cls
    echo.
    echo Starting Web Application...
    echo Flask server will run on http://localhost:5000
    echo Press Ctrl+C to stop the server
    echo.
    python web_app.py
) else if "%choice%"=="3" (
    cls
    echo.
    echo Starting Desktop GUI...
    echo.
    python gui_app.py
) else if "%choice%"=="4" (
    echo Goodbye!
    exit /b 0
) else (
    echo Invalid choice. Please enter 1-4.
    pause
)
