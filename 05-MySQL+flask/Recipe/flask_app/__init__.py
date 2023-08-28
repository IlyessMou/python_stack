from flask import Flask

app = Flask(__name__)
app.secret_key = "recipe"
DB_NAME = "recipes"
bcrypt = Bcrypt(app)