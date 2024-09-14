from flask_login import UserMixin
import mysql.connector as sql

BANCO = 'romerito_database'
def obter_conexao():
    conn = sql.connect(BANCO)
    return conn

class User(UserMixin):
    id: str
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha