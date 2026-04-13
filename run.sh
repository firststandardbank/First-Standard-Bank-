#!/bin/bash

# First Standard Bank - Launcher Script

echo "╔══════════════════════════════════════════════╗"
echo "║     🏦 First Standard Bank Application      ║"
echo "╚══════════════════════════════════════════════╝"
echo ""
echo "Select which interface you want to run:"
echo ""
echo "1) Console Demo     - Quick demonstration"
echo "2) Web App         - Browser-based interface (http://localhost:5000)"
echo "3) Desktop GUI     - Tkinter desktop application"
echo "4) Exit"
echo ""

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo ""
        echo "Starting Console Demo..."
        echo ""
        python main.py
        ;;
    2)
        echo ""
        echo "Starting Web Application..."
        echo "Flask server will run on http://localhost:5000"
        echo "Press Ctrl+C to stop the server"
        echo ""
        python web_app.py
        ;;
    3)
        echo ""
        echo "Starting Desktop GUI..."
        echo ""
        python gui_app.py
        ;;
    4)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice. Please enter 1-4."
        ;;
esac
