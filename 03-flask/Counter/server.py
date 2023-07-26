# app.py
from flask import Flask, render_template, session, redirect, url_for, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'counter' not in session:
        session['counter'] = 1

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'increment':
            session['counter'] += 1
        elif action == 'reset':
            session['counter'] = 1

    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session', methods=['GET', 'POST'])
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
