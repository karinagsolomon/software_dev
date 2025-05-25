from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secretkey123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:anchor05@localhost/demoDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class KoraUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200))

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']
        address = request.form['address']

        if KoraUser.query.filter_by(username=username).first():
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('register'))
        if KoraUser.query.filter_by(email=email).first():
            flash('Email already exists. Please choose a different one.')
            return redirect(url_for('register'))

        new_user = KoraUser(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
            address=address
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = KoraUser.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('checkout'))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/checkout')
def checkout():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('checkout.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)