from bank import Bank

# Example usage with persistent database
if __name__ == "__main__":
    print("=" * 60)
    print("First Standard Bank - Console Demo")
    print("=" * 60)
    
    # Initialize bank
    bank = Bank()
    
    # Create accounts
    print("\n1. Creating accounts...")
    bank.create_account("ACC001", "John Doe", 1000)
    bank.create_account("ACC002", "Jane Smith", 500)
    print("✓ Accounts created")
    
    # Display all accounts
    print("\n2. All Accounts:")
    for account in bank.get_all_accounts():
        print(f"   - {account['owner']} ({account['account_number']}): ${account['balance']:.2f}")
    
    # Perform transactions
    print("\n3. Performing transactions...")
    result = bank.deposit("ACC001", 500)
    print(f"   Deposit: {result}")
    
    result = bank.withdraw("ACC001", 200)
    print(f"   Withdrawal: {result}")
    
    # View account details
    print("\n4. Account Details:")
    account = bank.get_account_info("ACC001")
    print(f"   Account: {account['account_number']}")
    print(f"   Owner: {account['owner']}")
    print(f"   Balance: ${account['balance']:.2f}")
    
    # View transaction history
    print("\n5. Transaction History for ACC001:")
    transactions = bank.get_transaction_history("ACC001")
    for tx in transactions:
        print(f"   {tx['type']}: ${tx['amount']:.2f} -> Balance: ${tx['balance_after']:.2f}")
    
    print("\n" + "=" * 60)
    print("To use the full features:")
    print("  - Web App: python web_app.py (then visit http://localhost:5000)")
    print("  - GUI App: python gui_app.py")
    print("=" * 60)