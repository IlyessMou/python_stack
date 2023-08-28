from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask_app import DB_NAME 
from flask_app import app
from flask import session , flash
import re

bcrypt = Bcrypt(app)

class User:

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DB_NAME).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod 
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        
        results = connectToMySQL(DB_NAME).query_db(query, data)
        
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB_NAME).query_db(query, data)
        if results:
            return cls(results[0])
        return False
    
    @classmethod
    def register(cls, data):
        encrypted_password = bcrypt.generate_password_hash(data['password'])

        new_dict = {
            'firstname': data['firstname'],
            'lastname': data['lastname'],
            'email': data['email'],
            'password': encrypted_password
        }
        query = "INSERT INTO users (firstname, lastname, email, password) VALUES (%(firstname)s,%(lastname)s, %(email)s, %(password)s);"
        results = connectToMySQL(DB_NAME).query_db(query, new_dict)
        session['user_id'] = results
        return results
    
    
    @staticmethod
    def validation_registration(user):
        is_valid = True # Assuming the data provided is correct.
        user_in_db = User.get_by_email(user)
        if user_in_db:
            flash("Email already exists in database!")
            is_valid = False
        if not User.EMAIL_REGEX.match(user['email']): # username@something.cnth 
            flash("Invalid email.")
            is_valid = False
        if len(user['firstname']) < 3:
            flash("Firstname needs to be longer than 2 characters!")
            is_valid = False
        if len(user['lastname']) < 3:
            flash("Lastname needs to be longer than 2 characters!")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password too short!")
            is_valid = False
        if not user['password'] == user['confirm_password']:
            flash("Passwords don't match!")
            is_valid = False
        
        return is_valid
    
    @staticmethod
    def validation_login(user):
        is_valid = True
        user_in_db = User.get_by_email({'email' : user['email']})
        
        if not user_in_db:
            flash("Email is not associated with an account!")
            is_valid = False
        if not User.EMAIL_REGEX.match(user['email']): # username@something.cnth saldjfknlawef
            flash("Invalid email.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password too short!")
            is_valid = False
        if user_in_db:
            if not bcrypt.check_password_hash(user_in_db.password, user['password']):
                flash("Incorrect Password!")
                is_valid = False
        
        if is_valid == True:
            session['user_id'] = user_in_db.id

        return is_valid