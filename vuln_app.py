# app.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Vuln Test App"

@app.route('/search')
def search():
    q = request.args.get('q', '')
    # Vulnerable to XSS — reflects input without sanitization
    return f"You searched for: {q}"

@app.route('/login')
def login():
    username = request.args.get('username', '')
    # Vulnerable to SQLi — returns SQL error for injection patterns
    if "admin'" in username or "--" in username or "OR" in username.upper():
        return "SQL syntax error: near ''admin' --' at line 1"
    return "Login failed"

@app.route('/ping')
def ping():
    host = request.args.get('host', '')
    # Vulnerable to command injection — simulates command execution
    if ";" in host or "|" in host or "&&" in host:
        return "Command executed: " + host
    return "Ping to: " + host

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)