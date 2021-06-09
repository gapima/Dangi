from flask import Flask, render_template

app = Flask(__name__)

app_name = "Dangi"

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/login')
def login():
    return render_template('login.html') 

@app.route('/register')
def register():
    return render_template('register.html') 

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') 