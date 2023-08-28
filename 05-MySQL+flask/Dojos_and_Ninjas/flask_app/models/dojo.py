from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from flask_app import DATABASE_NAME

class Dojo:

    def __init__(self, data_dict) :
        self.id = data_dict["id"]
        self.name = data_dict["name"]
        self.created_at = data_dict["created_at"]
        self.updated_at = data_dict["updated_at"]
        self.My_ninjas=[]

    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM dojos;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        all_dojos = []
        for row in results:
            all_dojos.append(cls(row))
        return all_dojos
    
    @classmethod
    def create(cls,data_dict):
        query = """
                    INSERT INTO dojos (name)
                    VALUES (%(name)s);
                """
        result = connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
        return result
    @classmethod
    def get_one_by_id(cls, data_dict):
        query  = """SELECT * FROM dojos 
                    LEFT JOIN ninjas ON dojos.id  = ninjas.dojos_id 
                    WHERE dojos.id = %(id)s ;"""
        results  = connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
        if results:
            this_dojo = cls(results[0])
            for row in results :
                ninja_data ={
                    'id':row['ninjas.id'],
                    'dojos_id':row['dojos_id'],
                    'first_name': row['first_name'],
                    'last_name':row['last_name'],
                    'age':row['age'],
                    'created_at' : row['ninjas.created_at'],
                    'updated_at' : row['ninjas.updated_at']
                }
                ninja_instance = Ninja(ninja_data)
                this_dojo.My_ninjas.append(ninja_instance)
            return this_dojo
        return None