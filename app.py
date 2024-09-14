#Aplicativo principal
from flask  import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
