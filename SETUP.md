# Setup Guide - First Standard Bank

This guide will walk you through setting up the First Standard Bank application on your system.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git (for cloning the repository)

## Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd First-Standard-Bank
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Choose one of three options:

**Linux/macOS:**
```bash
chmod +x run.sh
./run.sh
```

**Windows:**
```bash
run.bat
```

**Or manually run any interface:**
```bash
python main.py      # Console demo
python web_app.py   # Web app (visit http://localhost:5000)
python gui_app.py   # Desktop GUI
```

---

## Platform-Specific Setup

### Windows

1. **Python Installation:**
   - Download Python 3.11+ from [python.org](https://www.python.org/downloads/)
   - ✅ Check "Add Python to PATH" during installation
   - Click "Install Now"

2. **Clone Repository:**
   ```bash
   git clone <repository-url>
   cd First-Standard-Bank
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Application:**
   - Double-click `run.bat` file
   - Or open Command Prompt in the folder and type: `python main.py`

### macOS

1. **Install Python (if not already installed):**
   ```bash
   # Using Homebrew
   brew install python@3.11
   ```

2. **Clone Repository:**
   ```bash
   git clone <repository-url>
   cd First-Standard-Bank
   ```

3. **Install Dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Run Application:**
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

### Linux (Ubuntu/Debian)

1. **Install Python and pip:**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-tk
   ```

2. **Clone Repository:**
   ```bash
   git clone <repository-url>
   cd First-Standard-Bank
   ```

3. **Install Dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Run Application:**
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

---

## Verifying Installation

Test that everything is working correctly:

```bash
python -c "import flask; print('Flask version:', flask.__version__)"
```

Expected output:
```
Flask version: 2.3.3
```

---

## Running Each Interface

### Console Demo

```bash
python main.py
```

This will demonstrate:
- Creating accounts
- Performing deposits and withdrawals
- Viewing account details
- Checking transaction history

**No additional setup needed** - runs completely offline.

### Web Application

```bash
python web_app.py
```

Then open your browser and visit: `http://localhost:5000`

**Features:**
- Create accounts via web form
- View all accounts
- Perform deposits/withdrawals
- View transaction history
- Beautiful responsive interface

**To access from another computer:**
- Find your computer's IP address
- Visit: `http://<your-ip>:5000` from another device on the same network

### Desktop GUI

```bash
python gui_app.py
```

**Features:**
- Tabbed interface for easy navigation
- All-accounts view
- Create account form
- Account management (deposit, withdraw)
- Transaction history viewer

**System Requirements:**
- Tkinter (usually included with Python)
  - If missing on Linux: `sudo apt install python3-tk`
  - If missing on macOS: `brew install python-tk@3.11` (replace 3.11 with your Python version)

---

## Troubleshooting

### Python Not Found

**Windows:**
- Reinstall Python and check "Add Python to PATH"
- Use `python` instead of `python3`

**macOS/Linux:**
- Use `python3` instead of `python`
- Check if Python is in PATH: `which python3`

### Port 5000 Already in Use

The web app might fail to start because port 5000 is busy:

```python
# Edit web_app.py, change the last line to:
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Use different port
```

Then run: `python web_app.py`

### Tkinter Not Found (GUI)

**Ubuntu/Debian:**
```bash
sudo apt install python3-tk
```

**macOS:**
```bash
brew install python-tk@3.11
# Replace 3.11 with your Python version
```

**Windows:**
- Reinstall Python
- During installation, ensure "tcl/tk and IDLE" is checked

### Database Already in Use

If you get database locking errors:

```bash
# Delete the database to start fresh (you'll lose all data)
rm bank.db      # macOS/Linux
del bank.db     # Windows
```

Then run the application again.

### `flask` Command Not Found

Instead of using `flask run`, use:
```bash
python web_app.py
```

---

## Development Setup

### Setting Up a Virtual Environment

Recommended for development:

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Running in Development Mode

The Flask app already runs in debug mode:

```bash
python web_app.py
# Output: Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

The server will:
- Auto-reload when you make code changes
- Show debug information on errors
- Enable the interactive debugger

---

## Getting Help

If you encounter issues:

1. Check this guide first
2. Review the main README.md for feature documentation
3. Check error messages carefully
4. Try running `python main.py` first (doesn't require Flask)
5. Verify Python version: `python --version`

---

## Next Steps

After successful installation:

1. Run the console demo to understand the features
2. Try the web app for a modern interface
3. Use the GUI for desktop applications
4. Read the main README.md for advanced features
5. Explore the code to understand the architecture

Happy Banking! 🏦
