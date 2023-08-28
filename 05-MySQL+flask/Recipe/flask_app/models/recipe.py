from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB_NAME 
from flask import flash
from flask_app.models import user
import re

class Recipe:

    NUMBER_REGEX = re.compile(r'^[0-9]+$')

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made_on = data['date_made_on']
        self.cook_time = data['cook_time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(DB_NAME).query_db(query)        
        recipes = []
        for row in results:
            # Creating an instance of the review
            recipe = cls(row)

            # Dictionary to create the User instance
            user_dict = {
                'id': row['users.id'],
                'firstname': row['firstname'],
                'lastname': row['lastname'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],}
            recipe.user = user.User(user_dict)
            recipes.append(recipe)
        return recipes
    
    
    
    @classmethod 
    def get_by_id(cls, data): 
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DB_NAME).query_db(query, data)
        print(results)
        if len(results) < 1:
            return False
        
        row = results[0]
        recipe = cls(row)
        
        user_dict = {
            'id': row['users.id'],
            'firstname': row['firstname'],
            'lastname': row['lastname'],
            'email': row['email'],
            'password': row['password'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at'],
        }

        recipe.user = user.User(user_dict)
        return recipe

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, cook_time, date_made_on, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(cook_time)s, %(date_made_on)s, %(user_id)s);"
        results = connectToMySQL(DB_NAME).query_db(query , data)
        return results
    
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, cook_time = %(cook_time)s, date_made_on = %(date_made_on)s WHERE id = %(id)s;"
        results = connectToMySQL(DB_NAME).query_db(query, data)
        return results
    
    @classmethod 
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DB_NAME).query_db(query, data)
    
    @staticmethod
    def validation(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Name is too short!","recipe")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description is too short!","recipe")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Instructions are too short!","recipe")
            is_valid = False 
        if (recipe['cook_time']!='yes' and recipe['cook_time']!='no' ):              
            flash("Cook time must be checked","recipe")
            is_valid = False
        if not recipe['date_made_on']:
            flash("enter the date made on","recipe")
            is_valid = False
        return is_valid
        