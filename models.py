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


# Inserir funções de controle de login










# Funções do banco de dados nas tabelas usuarios e livros

# SELECIONAR USER   
    @classmethod
    def select_data_user(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_usuarios WHERE usu_id=%s'
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchone()
        if dados:
            user = User(dados['nome'], dados['email'], dados['senha'])
            user.id = dados['id']

            cursor.close()
            conexao.close()

            return user

# SELECIONAR LIVRO  
    @classmethod
    def select_data_livro(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_livros WHERE liv_id=%s'
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchone()
        if dados:
            user = User(dados['titulo'], dados['genero'])
            user.id = dados['id']

            cursor.close()
            conexao.close()

            return user

# ATUALIZAR SENHA (n faz sentido att e-mail)  
    @classmethod
    def update_data_user(cls,id, senha):
        conexao = obter_conexao()
        try:
            cursor = conexao.cursor(dictionary=True)
            UPDATE = 'UPDATE tb_usuarios SET usu_senha=%s WHERE usu_id=%s'
            cursor.execute(UPDATE, (senha,id,))

            conexao.commit()
        except sql.connector.Error as e:
            print(f"Erro ao atualizar dados: {e}")

        finally:
            cursor.close()
            conexao.close()

# ATUALIZAR TITULO E GÊNERO 
    @classmethod
    def update_data_livro(cls,id, titulo, genero):
        conexao = obter_conexao()
        try:
            cursor = conexao.cursor(dictionary=True)
            UPDATE = 'UPDATE tb_livros SET liv_titulo=%s, liv_genero=%s WHERE liv_id=%s'
            cursor.execute(UPDATE, (titulo,genero,id,))

            conexao.commit()
        except sql.connector.Error as e:
            print(f"Erro ao atualizar dados: {e}")

        finally:
            cursor.close()
            conexao.close()

# DELETAR USUÁRIO   
    @classmethod
    def delete_data_user(cls, id):
        conexao = obter_conexao()
        try:
            cursor = conexao.cursor()
            DELETE = 'DELETE FROM tb_usuarios WHERE id=%s'
            cursor.execute(DELETE, (id,))
            conexao.commit()

        except sql.connector.Error as e:
            print(f"Erro ao deletar dados: {e}")

        finally:
            cursor.close()
            conexao.close()

# DELETAR LIVRO
    @classmethod
    def delete_data_livro(cls, id):
        conexao = obter_conexao()
        try:
            cursor = conexao.cursor()
            DELETE = 'DELETE FROM tb_livros WHERE id=%s'
            cursor.execute(DELETE, (id,))
            conexao.commit()

        except sql.connector.Error as e:
            print(f"Erro ao deletar dados: {e}")

        finally:
            cursor.close()
            conexao.close()

# INSERIR USER
    @classmethod
    def insert_data_user(cls, nome, email, senha):
        conexao = obter_conexao()
        try:
            cursor = conexao.cursor()
            INSERT = 'INSERT INTO tb_usuarios (usu_nome, usu_email, usu_senha) VALUES (%s, %s, %s)'
            cursor.execute(INSERT, (nome, email, senha,))
            conexao.commit()

        except sql.connector.Error as e:
            print(f"Erro ao inserir dados: {e}")

        finally:
            cursor.close()
            conexao.close()

# INSERIR LIVRO
    @classmethod
    def insert_data_livro(cls, titulo, genero):
        conexao = obter_conexao()
        try:
            cursor = conexao.cursor()
            INSERT = 'INSERT INTO tb_livros (liv_titulo, liv_genero) VALUES (%s, %s)'
            cursor.execute(INSERT, (titulo, genero))
            conexao.commit()

        except sql.connector.Error as e:
            print(f"Erro ao inserir dados: {e}")

        finally:
            cursor.close()
            conexao.close()