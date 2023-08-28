from flask import Flask
app = Flask(__name__)
app.secret_key = "secret-key"
DATABASE_NAME= "Dojos_and_Ninjas"