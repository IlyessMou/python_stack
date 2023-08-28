from flask import render_template, request, session, redirect
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')    
    logged_user = User.get_by_id({'id' : session['user_id']})
    result = Recipe.get_all()
    return render_template("dashboard.html", logged_user = logged_user, all_recipes = result)

@app.route('/recipes/new')
def get_create_page():
    logged_user = User.get_by_id({'id' : session['user_id']})
    return render_template('new_recipe.html', logged_user = logged_user)

@app.route('/recipes/new', methods = ['POST'])
def create():
    if not Recipe.validation(request.form):
        return redirect('/recipes/new')
    
    result = Recipe.create(request.form)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def show(id):
    logged_user = User.get_by_id({'id' : session['user_id']})
    recipe = Recipe.get_by_id({'id': id})
    return render_template('show_recipe.html', recipe = recipe,logged_user = logged_user)

@app.route('/recipes/edit/<int:id>')
def show_edit_page(id):
    logged_user = User.get_by_id({'id' : session['user_id']})
    recipe = Recipe.get_by_id({'id': id})
    return render_template('edit_recipe.html', recipe = recipe, logged_user = logged_user)

@app.route('/recipes/edit/<int:id>', methods = ['POST'])
def update(id):
    if not Recipe.validation(request.form):
        return redirect(f'/recipe/edit/{id}')
    data={'id':id,
          'name' :request.form['name'],
          'description' :request.form['description'],
          'instructions' :request.form['instructions'],
          'date_made_on' :request.form['date_made_on'],
          'cook_time' :request.form['cook_time'],      
          'user_id' : session['user_id']} 
    Recipe.update(data)
    return redirect("/dashboard")

@app.route('/recipes/delete/<int:id>')
def delete(id):
    result = Recipe.delete({'id': id})
    return redirect('/dashboard')