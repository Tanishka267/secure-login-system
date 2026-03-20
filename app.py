from flask import Flask, request
import re
import time
import hashlib

app = Flask(__name__)

users = {}
login_attempts = {}

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Password strength checker
def check_password_strength(password):
    if len(password) < 6:
        return "Weak"
    if (re.search("[A-Z]", password) and 
        re.search("[0-9]", password) and 
        re.search("[!@#$%^&*]", password)):
        return "Strong"
    return "Medium"

# Home page
@app.route('/')
def home():
    return """
    <h2>Secure Login System</h2>
    <a href='/register'>Register</a><br><br>
    <a href='/login'>Login</a>
    """

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return " Username already exists! <br><a href='/register'>Try again</a>"

        strength = check_password_strength(password)

        if strength == "Weak":
            return " Weak password! <br><a href='/register'>Try again</a>"

        users[username] = hash_password(password)
        return " Registered successfully! <br><a href='/login'>Login</a>"

    return """
    <h2>Register</h2>
    <form method='post'>
        Username: <input type='text' name='username'><br><br>
        Password: <input type='password' name='password'><br><br>
        <input type='submit' value='Register'>
    </form>
    """

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in login_attempts:
            attempts, last_time = login_attempts[username]
            if attempts >= 3 and time.time() - last_time < 30:
                return "🔒 Account locked! Try later."

        if username in users and users[username] == hash_password(password):
            login_attempts[username] = (0, time.time())
            return f" Welcome {username}!"
        else:
            attempts = login_attempts.get(username, (0, 0))[0]
            login_attempts[username] = (attempts + 1, time.time())
            return " Invalid credentials! <br><a href='/login'>Try again</a>"

    return """
    <h2>Login</h2>
    <form method='post'>
        Username: <input type='text' name='username'><br><br>
        Password: <input type='password' name='password'><br><br>
        <input type='submit' value='Login'>
    </form>
    """

if __name__ == '__main__':
    app.run(debug=True)
