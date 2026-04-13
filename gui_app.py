import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from bank import Bank
import uuid

class BankingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("First Standard Bank - Desktop App")
        self.root.geometry("900x700")
        self.bank = Bank()
        
        self.setup_ui()

    def setup_ui(self):
        # Main notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Tab 1: View Accounts
        self.accounts_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.accounts_tab, text='All Accounts')
        self.setup_accounts_tab()
        
        # Tab 2: Create Account
        self.create_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.create_tab, text='Create Account')
        self.setup_create_tab()
        
        # Tab 3: Manage Account
        self.manage_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.manage_tab, text='Manage Account')
        self.setup_manage_tab()

    def setup_accounts_tab(self):
        # Refresh button
        refresh_btn = ttk.Button(self.accounts_tab, text='Refresh', command=self.refresh_accounts)
        refresh_btn.pack(pady=10)
        
        # Treeview for accounts
        columns = ('Account Number', 'Owner', 'Balance', 'Created')
        self.accounts_tree = ttk.Treeview(self.accounts_tab, columns=columns, height=20)
        self.accounts_tree.column('#0', width=0, stretch=tk.NO)
        self.accounts_tree.column('Account Number', anchor=tk.W, width=200)
        self.accounts_tree.column('Owner', anchor=tk.W, width=150)
        self.accounts_tree.column('Balance', anchor=tk.E, width=100)
        self.accounts_tree.column('Created', anchor=tk.W, width=200)
        
        self.accounts_tree.heading('#0', text='', anchor=tk.W)
        self.accounts_tree.heading('Account Number', text='Account Number', anchor=tk.W)
        self.accounts_tree.heading('Owner', text='Owner', anchor=tk.W)
        self.accounts_tree.heading('Balance', text='Balance', anchor=tk.E)
        self.accounts_tree.heading('Created', text='Created', anchor=tk.W)
        
        scrollbar = ttk.Scrollbar(self.accounts_tab, orient=tk.VERTICAL, command=self.accounts_tree.yview)
        self.accounts_tree.configure(yscroll=scrollbar.set)
        
        self.accounts_tree.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        
        self.refresh_accounts()

    def refresh_accounts(self):
        for item in self.accounts_tree.get_children():
            self.accounts_tree.delete(item)
        
        accounts = self.bank.get_all_accounts()
        for account in accounts:
            self.accounts_tree.insert('', 'end', values=(
                account['account_number'],
                account['owner'],
                f"${account['balance']:.2f}",
                account['created_at']
            ))

    def setup_create_tab(self):
        frame = ttk.LabelFrame(self.create_tab, text='Create New Account', padding=20)
        frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Owner name
        ttk.Label(frame, text='Owner Name:').grid(row=0, column=0, sticky='w', pady=5)
        self.owner_entry = ttk.Entry(frame, width=40)
        self.owner_entry.grid(row=0, column=1, sticky='ew', pady=5)
        
        # Initial balance
        ttk.Label(frame, text='Initial Balance ($):').grid(row=1, column=0, sticky='w', pady=5)
        self.balance_entry = ttk.Entry(frame, width=40)
        self.balance_entry.insert(0, '0')
        self.balance_entry.grid(row=1, column=1, sticky='ew', pady=5)
        
        # Create button
        create_btn = ttk.Button(frame, text='Create Account', command=self.create_account)
        create_btn.grid(row=2, column=0, columnspan=2, pady=20)
        
        frame.columnconfigure(1, weight=1)

    def create_account(self):
        owner = self.owner_entry.get().strip()
        balance_str = self.balance_entry.get().strip()
        
        if not owner:
            messagebox.showerror('Error', 'Please enter owner name')
            return
        
        try:
            balance = float(balance_str) if balance_str else 0
            if balance < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid balance')
            return
        
        account_number = str(uuid.uuid4())[:12]
        success = self.bank.create_account(account_number, owner, balance)
        
        if success:
            messagebox.showinfo('Success', f'Account created!\nAccount Number: {account_number}')
            self.owner_entry.delete(0, tk.END)
            self.balance_entry.delete(0, tk.END)
            self.balance_entry.insert(0, '0')
            self.refresh_accounts()
        else:
            messagebox.showerror('Error', 'Failed to create account')

    def setup_manage_tab(self):
        # Account selection
        frame = ttk.LabelFrame(self.manage_tab, text='Select Account', padding=20)
        frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(frame, text='Account Number:').pack(side=tk.LEFT, padx=5)
        self.manage_account_entry = ttk.Entry(frame, width=30)
        self.manage_account_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame, text='Load Account', command=self.load_account).pack(side=tk.LEFT, padx=5)
        
        # Account info
        self.info_frame = ttk.LabelFrame(self.manage_tab, text='Account Info', padding=10)
        self.info_frame.pack(fill='x', padx=10, pady=10)
        
        self.info_text = tk.Text(self.info_frame, height=5, width=80)
        self.info_text.pack(fill='both', expand=True)
        
        # Transactions
        ops_frame = ttk.LabelFrame(self.manage_tab, text='Transactions', padding=10)
        ops_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(ops_frame, text='Amount ($):').pack(side=tk.LEFT, padx=5)
        self.amount_entry = ttk.Entry(ops_frame, width=15)
        self.amount_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(ops_frame, text='Deposit', command=self.deposit).pack(side=tk.LEFT, padx=5)
        ttk.Button(ops_frame, text='Withdraw', command=self.withdraw).pack(side=tk.LEFT, padx=5)
        
        # History
        history_frame = ttk.LabelFrame(self.manage_tab, text='Transaction History', padding=10)
        history_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.history_text = scrolledtext.ScrolledText(history_frame, height=15, width=80)
        self.history_text.pack(fill='both', expand=True)

    def load_account(self):
        account_number = self.manage_account_entry.get().strip()
        
        if not account_number:
            messagebox.showerror('Error', 'Please enter account number')
            return
        
        account = self.bank.get_account_info(account_number)
        if not account:
            messagebox.showerror('Error', 'Account not found')
            return
        
        # Display account info
        self.info_text.delete(1.0, tk.END)
        info = f"""Account Number: {account['account_number']}
Owner: {account['owner']}
Balance: ${account['balance']:.2f}
Created: {account['created_at']}"""
        self.info_text.insert(1.0, info)
        
        # Display transaction history
        self.history_text.delete(1.0, tk.END)
        transactions = self.bank.get_transaction_history(account_number)
        if transactions:
            self.history_text.insert(1.0, 'ID\tType\tAmount\tBalance After\tTimestamp\n')
            self.history_text.insert(tk.END, '-' * 80 + '\n')
            for tx in transactions:
                line = f"{tx['id']}\t{tx['type']}\t${tx['amount']:.2f}\t${tx['balance_after']:.2f}\t{tx['timestamp']}\n"
                self.history_text.insert(tk.END, line)
        else:
            self.history_text.insert(1.0, 'No transactions')

    def deposit(self):
        account_number = self.manage_account_entry.get().strip()
        amount_str = self.amount_entry.get().strip()
        
        if not account_number or not amount_str:
            messagebox.showerror('Error', 'Please enter account number and amount')
            return
        
        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror('Error', 'Invalid amount')
            return
        
        result = self.bank.deposit(account_number, amount)
        if result['success']:
            messagebox.showinfo('Success', f'Deposited ${amount:.2f}\nNew Balance: ${result["balance"]:.2f}')
            self.amount_entry.delete(0, tk.END)
            self.load_account()
            self.refresh_accounts()
        else:
            messagebox.showerror('Error', result['error'])

    def withdraw(self):
        account_number = self.manage_account_entry.get().strip()
        amount_str = self.amount_entry.get().strip()
        
        if not account_number or not amount_str:
            messagebox.showerror('Error', 'Please enter account number and amount')
            return
        
        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror('Error', 'Invalid amount')
            return
        
        result = self.bank.withdraw(account_number, amount)
        if result['success']:
            messagebox.showinfo('Success', f'Withdrew ${amount:.2f}\nNew Balance: ${result["balance"]:.2f}')
            self.amount_entry.delete(0, tk.END)
            self.load_account()
            self.refresh_accounts()
        else:
            messagebox.showerror('Error', result['error'])

if __name__ == '__main__':
    root = tk.Tk()
    app = BankingGUI(root)
    root.mainloop()
