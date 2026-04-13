from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from bank import Bank
import uuid
from functools import wraps

app = Flask(__name__)
app.secret_key = 'fsb-secret-key-2024'
bank = Bank()

# Demo users
DEMO_USERS = {
    'admin': 'admin123',
    'user1': 'password123',
    'user2': 'password456'
}

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if username in DEMO_USERS and DEMO_USERS[username] == password:
            session['username'] = username
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'Invalid credentials'}), 401
    
    if 'username' in session:
        return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    accounts = bank.get_all_accounts()
    return render_template('index.html', accounts=accounts, username=session.get('username'))

@app.route('/account/<account_number>')
@login_required
def view_account(account_number):
    account = bank.get_account_info(account_number)
    if not account:
        return "Account not found", 404
    
    transactions = bank.get_transaction_history(account_number)
    return render_template('account.html', account=account, transactions=transactions, username=session.get('username'))

@app.route('/create', methods=['GET', 'POST'])
@login_required
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
@login_required
def deposit(account_number):
    data = request.get_json()
    amount = float(data.get('amount', 0))
    result = bank.deposit(account_number, amount)
    
    if result['success']:
        return jsonify({'success': True, 'balance': result['balance']})
    else:
        return jsonify({'success': False, 'error': result['error']}), 400

@app.route('/withdraw/<account_number>', methods=['POST'])
@login_required
def withdraw(account_number):
    data = request.get_json()
    amount = float(data.get('amount', 0))
    result = bank.withdraw(account_number, amount)
    
    if result['success']:
        return jsonify({'success': True, 'balance': result['balance']})
    else:
        return jsonify({'success': False, 'error': result['error']}), 400

@app.route('/api/accounts')
@login_required
def api_accounts():
    accounts = bank.get_all_accounts()
    return jsonify(accounts)

@app.route('/api/account/<account_number>')
@login_required
def api_account(account_number):
    account = bank.get_account_info(account_number)
    if account:
        return jsonify(account)
    return jsonify({'error': 'Account not found'}), 404

@app.route('/api/transactions/<account_number>')
@login_required
def api_transactions(account_number):
    transactions = bank.get_transaction_history(account_number)
    return jsonify(transactions)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
