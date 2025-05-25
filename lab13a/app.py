"""
Karina Solomon
Lab 13: Flash Application
"""
from flask import Flask, session, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
import os
# create an object 'app' from the Flask module. 
# __name__ set to __main__ if the script is running directly from the main file
app = Flask(__name__) 
# connection to PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'postgresql://postgres:anchor05@localhost/demoDB')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:anchor05@localhost/demoDB' # replace pword with 'password' before submission
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

# create a DB object
db = SQLAlchemy(app)

# define a model (create table in the demoDB database)
class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)

# set the routing to the main page
# route decorator is used to access the root URL

# @app.route('/')
# def home():
#    return "PostgreSQL integrated with Flask!"

@app.route('/', methods=['GET', 'POST'])
def index():
    name = "Karina"
    checkfruit = 'pomelo'
    fruits = ['apple', 'banana', 'cherry']
    if request.method == 'POST':
        return 'Entered password = '+request.form['password']
    return render_template('index.html', username=name, listfruits=fruits, checkfruit=checkfruit)
    
@app.route('/profile')
def profile():
    name = "Karina Solomon"
    return render_template('profile.html', username=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/base')
def base():
    return render_template('base.html')

# define employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(20), unique=True,
    nullable=False)
    employee_name = db.Column(db.String(100), nullable=False)

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        try:
            form = request.form
            emp_name = form['employee_name']
            emp_id = form['employee_id']
            # Check if employee already exists by name (or use employee_id if that's unique)
            existing_employee = Employee.query.filter_by(employee_name=emp_name).first()
            existing_id = Employee.query.filter_by(employee_id = emp_id).first()
            if existing_employee:
                return f"Employee with name '{emp_name}' already exists!", 400
            if existing_id:
                return f"Employee with id '{emp_id}' already exists!", 400
            # Create new Employee object and add to database
            new_employee = Employee(employee_name=emp_name, employee_id=emp_id)
            # store new employee name in session
            session['employee1'] = new_employee.employee_name
            # add new employee to the database
            db.session.add(new_employee)
            db.session.commit()
            # message using flash
            return request.form['employee_name'] + ' successfully added'
        except:
            flash("Fail to insert data! Try again")
    return render_template('users.html')

@app.route('/add_employee', methods=['POST'])
def add_employee():
    new_employee = [{'employee_name': 'Karina'}] # Example input
    session['employee1'] = new_employee[0]['employee_name']
    return redirect(url_for('show_employee'))

@app.route('/show_employee')
def show_employee():
    return f"First employee: {session.get('employee1', 'Not set')}"

@app.route('/quotes')
def quotes():
    return redirect(url_for('index'))

# app to run if you execute the file directly (not imported)
if __name__ == '__main__':
    # Create the tables
    with app.app_context():db.create_all()
    app.run(debug=True)
