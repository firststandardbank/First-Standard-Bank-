# First Standard Bank 🏦

A comprehensive banking application built in Python with multiple interfaces: console, web, and desktop GUI. Features persistent database storage, transaction history, account management, and more.

## Features

✨ **Core Banking System**
- Create and manage multiple bank accounts
- Deposit and withdraw funds with validation
- Real-time balance updates
- Transaction history with timestamps
- In-memory or persistent SQLite database

🌐 **Web Application** (Flask)
- Beautiful responsive web interface
- Create accounts and manage balances
- View all accounts and transactions
- RESTful API endpoints
- Real-time updates

🖥️ **Desktop GUI** (Tkinter)
- Multi-tab interface for all operations
- Account creation and management
- Quick deposit/withdraw operations
- Transaction history viewer
- Real-time balance display

💾 **Data Persistence**
- SQLite database for permanent storage
- Transaction logging
- Account history tracking
- Data migration support

## Project Structure

```
First-Standard-Bank/
├── bank.py              # Core banking logic & database
├── web_app.py           # Flask web application
├── gui_app.py           # Tkinter desktop GUI
├── main.py              # Console demo script
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates for web app
│   ├── index.html
│   ├── create_account.html
│   └── account.html
└── README.md
```

## Installation

### Requirements
- Python 3.7+
- pip (Python package manager)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd First-Standard-Bank
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Option 1: Console Application

Run the console demo to see the banking system in action:

```bash
python main.py
```

Output:
```
============================================================
First Standard Bank - Console Demo
============================================================

1. Creating accounts...
✓ Accounts created

2. All Accounts:
   - John Doe (ACC001): $1000.00
   - Jane Smith (ACC002): $500.00

3. Performing transactions...
   Deposit: {'success': True, 'balance': 1500.0}
   Withdrawal: {'success': True, 'balance': 1300.0}

... and more
```

### Option 2: Web Application

Start the Flask web server:

```bash
python web_app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

**Features:**
- View all accounts on the dashboard
- Create new accounts with initial deposits
- View detailed account information
- Perform deposits and withdrawals
- View complete transaction history

### Option 3: Desktop GUI

Launch the Tkinter desktop application:

```bash
python gui_app.py
```

**Interface Tabs:**
1. **All Accounts** - View all bank accounts
2. **Create Account** - Create new accounts with initial balance
3. **Manage Account** - Select account, perform transactions, view history

## API Endpoints (Web App)

- `GET /` - Home page with all accounts
- `GET /create` - Create account form
- `POST /create` - Submit account creation
- `GET /account/<account_number>` - View account details
- `POST /deposit/<account_number>` - Deposit funds
- `POST /withdraw/<account_number>` - Withdraw funds
- `GET /api/accounts` - Get all accounts (JSON)
- `GET /api/account/<account_number>` - Get account info (JSON)
- `GET /api/transactions/<account_number>` - Get transaction history (JSON)

## Database Schema

### Accounts Table
```sql
CREATE TABLE accounts (
    account_number TEXT PRIMARY KEY,
    owner TEXT NOT NULL,
    balance REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

### Transactions Table
```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number TEXT NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL,
    balance_after REAL NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## Core Classes & Methods

### Bank Class

```python
bank = Bank('bank.db')  # Initialize with database path

# Account Management
bank.create_account('ACC001', 'John Doe', 1000)
bank.account_exists('ACC001')
bank.get_account_info('ACC001')
bank.get_all_accounts()

# Transactions
bank.deposit('ACC001', 500)           # Returns {'success': True, 'balance': ...}
bank.withdraw('ACC001', 200)          # Returns {'success': True, 'balance': ...}
bank.get_balance('ACC001')

# History
bank.get_transaction_history('ACC001', limit=50)
```

## Example Usage in Code

```python
from bank import Bank

# Initialize bank
bank = Bank()

# Create an account
bank.create_account('ACC001', 'Alice Johnson', 1000)

# Perform transactions
bank.deposit('ACC001', 500)
bank.withdraw('ACC001', 250)

# Check balance
balance = bank.get_balance('ACC001')
print(f"Current balance: ${balance:.2f}")

# View history
history = bank.get_transaction_history('ACC001')
for transaction in history:
    print(f"{transaction['type']}: ${transaction['amount']:.2f}")
```

## Error Handling

All operations return dictionaries with success status:

```python
result = bank.deposit('INVALID', 100)
# Returns: {'success': False, 'error': 'Account not found'}

result = bank.withdraw('ACC001', 99999)
# Returns: {'success': False, 'error': 'Insufficient funds'}
```

## Security Notes

⚠️ **Important for Production:**
- Change Flask secret key in `web_app.py`
- Implement user authentication
- Use encrypted database connections
- Add input validation and sanitization
- Implement rate limiting
- Use HTTPS in production
- Add proper authorization checks

## Testing

You can test the system by:

1. Running the console demo: `python main.py`
2. Starting the web app and using the browser interface
3. Launching the GUI and testing each tab
4. Checking `bank.db` with SQLite to verify database state

## Troubleshooting

**Port 5000 already in use:**
```bash
python web_app.py --port 5001
```

**Database locked error:**
- Close other instances of the application
- Delete `bank.db` to reset (will lose all data)

**Tkinter not available:**
```bash
# On Ubuntu/Debian:
sudo apt-get install python3-tk

# On macOS:
brew install python-tk@3.11  # replace with your Python version

# On Windows:
# Usually included with Python, reinstall if missing
```

## Future Enhancements

- [ ] User authentication and authorization
- [ ] Multiple currencies support
- [ ] Interest calculation
- [ ] Loan management
- [ ] API documentation (Swagger/OpenAPI)
- [ ] Unit and integration tests
- [ ] Docker containerization
- [ ] Database migrations
- [ ] Admin dashboard
- [ ] Mobile app (React Native)

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:
- Create an issue on GitHub
- Check existing documentation
- Review code comments and examples

---

**Made with ❤️ - First Standard Bank**