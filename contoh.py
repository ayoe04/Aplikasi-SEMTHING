from flask import Flask
from flask import escape
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/coba')
def coba():
    return render_template('coba.html')

# @app.route('/chatbot')
# def chatbot():
#     return render_template('chatbot.py')

app.run(debug=True)