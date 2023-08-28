from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def log_and_reg():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('log_and_reg.html')



@app.route('/register', methods=['POST'])
def register():    
    if not User.validation_registration(request.form):
        return redirect("/")    
    User.register(request.form)
    return redirect("/dashboard")



@app.route('/login', methods=['POST'])
def login():
    if not User.validation_login(request.form):
        return redirect("/")
    
    return redirect("/dashboard")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
    