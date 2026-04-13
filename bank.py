import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

class Bank:
    def __init__(self, db_path='bank.db'):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Accounts table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_number TEXT PRIMARY KEY,
                owner TEXT NOT NULL,
                balance REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Transactions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_number TEXT NOT NULL,
                transaction_type TEXT NOT NULL,
                amount REAL NOT NULL,
                balance_after REAL NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_number) REFERENCES accounts(account_number)
            )
        ''')
        
        conn.commit()
        conn.close()

    def create_account(self, account_number: str, owner: str, initial_balance: float = 0) -> bool:
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO accounts (account_number, owner, balance) VALUES (?, ?, ?)',
                (account_number, owner, initial_balance)
            )
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            return False

    def account_exists(self, account_number: str) -> bool:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM accounts WHERE account_number = ?', (account_number,))
        exists = cursor.fetchone() is not None
        conn.close()
        return exists

    def deposit(self, account_number: str, amount: float) -> Dict[str, any]:
        if not self.account_exists(account_number):
            return {'success': False, 'error': 'Account not found'}
        
        if amount <= 0:
            return {'success': False, 'error': 'Deposit amount must be positive'}
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute('UPDATE accounts SET balance = balance + ? WHERE account_number = ?',
                          (amount, account_number))
            cursor.execute('SELECT balance FROM accounts WHERE account_number = ?', (account_number,))
            new_balance = cursor.fetchone()[0]
            
            cursor.execute(
                'INSERT INTO transactions (account_number, transaction_type, amount, balance_after) VALUES (?, ?, ?, ?)',
                (account_number, 'DEPOSIT', amount, new_balance)
            )
            
            conn.commit()
            return {'success': True, 'balance': new_balance}
        finally:
            conn.close()

    def withdraw(self, account_number: str, amount: float) -> Dict[str, any]:
        if not self.account_exists(account_number):
            return {'success': False, 'error': 'Account not found'}
        
        if amount <= 0:
            return {'success': False, 'error': 'Withdrawal amount must be positive'}
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT balance FROM accounts WHERE account_number = ?', (account_number,))
            current_balance = cursor.fetchone()[0]
            
            if amount > current_balance:
                return {'success': False, 'error': 'Insufficient funds'}
            
            cursor.execute('UPDATE accounts SET balance = balance - ? WHERE account_number = ?',
                          (amount, account_number))
            cursor.execute('SELECT balance FROM accounts WHERE account_number = ?', (account_number,))
            new_balance = cursor.fetchone()[0]
            
            cursor.execute(
                'INSERT INTO transactions (account_number, transaction_type, amount, balance_after) VALUES (?, ?, ?, ?)',
                (account_number, 'WITHDRAWAL', amount, new_balance)
            )
            
            conn.commit()
            return {'success': True, 'balance': new_balance}
        finally:
            conn.close()

    def get_balance(self, account_number: str) -> Optional[float]:
        if not self.account_exists(account_number):
            return None
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT balance FROM accounts WHERE account_number = ?', (account_number,))
        balance = cursor.fetchone()[0]
        conn.close()
        return balance

    def get_account_info(self, account_number: str) -> Optional[Dict]:
        if not self.account_exists(account_number):
            return None
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT account_number, owner, balance, created_at FROM accounts WHERE account_number = ?',
                      (account_number,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return {
                'account_number': result[0],
                'owner': result[1],
                'balance': result[2],
                'created_at': result[3]
            }
        return None

    def get_transaction_history(self, account_number: str, limit: int = 50) -> List[Dict]:
        if not self.account_exists(account_number):
            return []
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id, transaction_type, amount, balance_after, timestamp FROM transactions WHERE account_number = ? ORDER BY timestamp DESC LIMIT ?',
            (account_number, limit)
        )
        rows = cursor.fetchall()
        conn.close()
        
        return [
            {
                'id': row[0],
                'type': row[1],
                'amount': row[2],
                'balance_after': row[3],
                'timestamp': row[4]
            }
            for row in rows
        ]

    def get_all_accounts(self) -> List[Dict]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT account_number, owner, balance, created_at FROM accounts ORDER BY created_at DESC')
        rows = cursor.fetchall()
        conn.close()
        
        return [
            {
                'account_number': row[0],
                'owner': row[1],
                'balance': row[2],
                'created_at': row[3]
            }
            for row in rows
        ]
