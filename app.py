#Aplicativo principal
from flask import Flask, render_template, url_for, redirect, request
from flask_login import LoginManager, login_required, login_user, logout_user
from models import User
from werkzeug.security import generate_password_hash, check_password_hash



login_manager = LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPERMEGADIFICIL'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)





@app.route('/', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        user = User.get_by_email(email)

        if user and check_password_hash(user["senha"], senha):
            login_user(user)

            return redirect(url_for('inicial'))
    return render_template('index.html')

@app.route('/cadastro', methods = ["POST", "GET"])
def cadastro():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        nome = request.form["nome"]
        hash = generate_password_hash(senha)

        #Cadastrar usuário nop db e depois pegar ele em objeto

        login_user(user)
        return redirect(url_for("inicial.html"))
    return render_template('cadastro.html')




@app.route("/inicial")
@login_required
def inicial():
    return render_template("inicial.html")







@app.route("/livros")
@login_required
def livros():
    return render_template("livros.html")



@app.route("/contatos")
@login_required
def contatos():
    return render_template("contatos.html")



@app.route("/conversas")
@login_required
def conversas():
    return render_template("conversas.html")





@app.route("/logout", methods=['POST', 'GET'])
@login_required
def logout():
    if request.method == "POST":
        logout_user()
    return render_template("logout.html")