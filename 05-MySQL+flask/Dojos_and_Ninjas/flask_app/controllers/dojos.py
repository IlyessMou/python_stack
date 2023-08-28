from flask_app import app
from flask import render_template , request, redirect
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    return render_template("index.html", dojos = all_dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/')

@app.route('/dojos/<int:dojos_id>')
def show_one_dojo(dojos_id):
    dojo_instance = Dojo.get_one_by_id({'id': dojos_id})
    return render_template('one_dojo.html', dojo = dojo_instance)