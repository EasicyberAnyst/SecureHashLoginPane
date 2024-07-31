from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import hashlib
from config import DATABASE, SECRET_KEY, CERT_PATH, KEY_PATH

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_db():
    with get_db() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
        conn.commit()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with get_db() as conn:
            try:
                conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
                conn.commit()
                flash('Registration successful. Please log in.', 'success')
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash('Username already exists. Please choose another.', 'danger')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with get_db() as conn:
            user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password)).fetchone()
            if user:
                session['user_id'] = user[0]
                session['username'] = user[1]
                flash('Login successful.', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password.', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return f"Welcome{session['username']}!"

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    create_db()
    app.run(host='CyptSha256', port=5050, ssl_context=(CERT_PATH, KEY_PATH), debug=True)
