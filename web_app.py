from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from bank import Bank
import uuid

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'
bank = Bank()

@app.route('/')
def index():
    accounts = bank.get_all_accounts()
    return render_template('index.html', accounts=accounts)

@app.route('/account/<account_number>')
def view_account(account_number):
    account = bank.get_account_info(account_number)
    if not account:
        return "Account not found", 404
    
    transactions = bank.get_transaction_history(account_number)
    return render_template('account.html', account=account, transactions=transactions)

@app.route('/create', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        data = request.get_json()
        owner = data.get('owner')
        initial_balance = float(data.get('initial_balance', 0))
        account_number = str(uuid.uuid4())[:12]
        
        success = bank.create_account(account_number, owner, initial_balance)
        if success:
            return jsonify({'success': True, 'account_number': account_number})
        else:
            return jsonify({'success': False, 'error': 'Failed to create account'}), 400
    
    return render_template('create_account.html')

@app.route('/deposit/<account_number>', methods=['POST'])
def deposit(account_number):
    data = request.get_json()
    amount = float(data.get('amount', 0))
    result = bank.deposit(account_number, amount)
    
    if result['success']:
        return jsonify({'success': True, 'balance': result['balance']})
    else:
        return jsonify({'success': False, 'error': result['error']}), 400

@app.route('/withdraw/<account_number>', methods=['POST'])
def withdraw(account_number):
    data = request.get_json()
    amount = float(data.get('amount', 0))
    result = bank.withdraw(account_number, amount)
    
    if result['success']:
        return jsonify({'success': True, 'balance': result['balance']})
    else:
        return jsonify({'success': False, 'error': result['error']}), 400

@app.route('/api/accounts')
def api_accounts():
    accounts = bank.get_all_accounts()
    return jsonify(accounts)

@app.route('/api/account/<account_number>')
def api_account(account_number):
    account = bank.get_account_info(account_number)
    if account:
        return jsonify(account)
    return jsonify({'error': 'Account not found'}), 404

@app.route('/api/transactions/<account_number>')
def api_transactions(account_number):
    transactions = bank.get_transaction_history(account_number)
    return jsonify(transactions)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
