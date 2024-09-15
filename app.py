#Aplicativo principal
from flask import Flask, render_template, url_for, redirect, request
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
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

        user = User.select_data_user_email(email)
        hash = user.senha
        if user and check_password_hash(hash, senha):
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

        User.insert_data_user(nome, email, hash)
        user = User.select_data_user_email(email)
        login_user(user)
        return redirect(url_for("inicial"))
    return render_template('cadastro.html')




@app.route("/inicial")
@login_required
def inicial():
    user = current_user.nome
    return render_template("inicial.html", user = user)







@app.route("/livros", methods = ["POST", "GET"])
@login_required
def livros():

    if request.method == "POST":
        titulo = request.form["titulo"]
        genero = request.form["genero"]
        id = current_user.id
        User.insert_data_livro(titulo, genero, id)

    id = current_user.id
    livros = User.select_data_livros(id)
    return render_template("livros.html", livros = livros)

@app.route('/<int:id>/remove_peca', methods=['POST'])
@login_required
def remove_livro(id):
    User.delete_data_livro(id)
    return redirect(url_for("livros"))





@app.route("/contatos", methods = ["POST", "GET"])
@login_required
def contatos():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        id = current_user.id
        User.insert_data_contato(nome, email, id)
    
    id = current_user.id
    contatos = User.select_data_contatos(id)
    return render_template("contatos.html", contatos = contatos)

@app.route('/<int:id>/remove_contato', methods=['POST'])
@login_required
def remove_contato(id):
    User.delete_data_contato(id)
    return redirect(url_for("contatos"))





@app.route("/conversas", methods = ["POST", "GET"])
@login_required
def conversas():
    if request.method == "POST":
        contato = request.form["contato"]
        id_contato = User.select_data_contato_email(contato)['id']
        id = current_user.id
        conteudo = request.form["conteudo"]
        User.insert_data_conversa(id_contato,id,conteudo)
    id = current_user.id
    contatos = User.select_data_contatos(id)

    return render_template("conversas.html", contatos = contatos)





@app.route("/logout", methods=['POST', 'GET'])
@login_required
def logout():
    if request.method == "POST":
        logout_user()
        return redirect(url_for("login"))
    return render_template("logout.html")