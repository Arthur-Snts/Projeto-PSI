from flask_login import UserMixin
import mysql.connector as sql

def obter_conexao():
    db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'biblioteca'
}
    conn = sql.connect(**db_config)
    return conn

class User(UserMixin):
    id: str
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Inserir funções de controle de login

    @classmethod
    def get(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        SELECT = 'SELECT * FROM tb_usuarios WHERE usu_id=%s'
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchone()
        if dados:
            user = User(dados[1],dados[2], dados[3])
            user.id = dados[0]
        else: 
            user = None
        return user








# Funções do banco de dados nas tabelas usuarios e livros

# SELECIONAR USER POR EMAIL   
    @classmethod
    def select_data_user_email(cls, email):
        conexao = obter_conexao()
        cursor = conexao.cursor(buffered=True)
        SELECT = 'SELECT * FROM tb_usuarios WHERE usu_email=%s'
        cursor.execute(SELECT, (email,))
        dados = cursor.fetchone()
        if dados:
            user = User(dados[1], dados[2], dados[3])
            user.id = dados[0]

            conexao.commit()
            cursor.close()

            return user
    
# SELECIONAR USER POR ID   
    @classmethod
    def select_data_user_id(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_usuarios WHERE usu_id=%s'
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchone()
        if dados:
            user = User(dados['usu_nome'], dados['usu_email'], dados['usu_senha'])
            user.id = dados['usu_id']

            cursor.close()
            conexao.close()

            return user
        
    # SELECIONAR CONVERSAS  
    @classmethod
    def select_data_conversas(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_usuarios WHERE msg_usuario_to=%s OR msg_usuario_from=%s ORDER BY msg_data_envio DESC'
        cursor.execute(SELECT, (id,id))
        dados = cursor.fetchall()

        cursor.close()
        conexao.close()

        return dados

# SELECIONAR LIVRO  
    @classmethod
    def select_data_livro(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_livros WHERE liv_id=%s'
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchone()
        if dados:
            user = User(dados['liv_titulo'], dados['liv_genero'])
            user.id = dados['liv_id']

            cursor.close()
            conexao.close()

            return user

# SELECIONAR LIVROS       
    @classmethod
    def select_data_livros(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_livros WHERE liv_usuarios_id=%s'
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchall()
        

        return dados
    
# SELECIONAR CONTATOS       
    @classmethod
    def select_data_contatos(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_contatos WHERE con_usuarios_id=%s'
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchall()
        

        return dados
    
    # SELECIONAR CONTATO 
    @classmethod
    def select_data_contato(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_contatos WHERE con_usuario_id=%s'
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchone()
        if dados:
            user = User(dados['con_nome'], dados['con_email'])
            user.id = dados["con_id"]

            cursor.close()
            conexao.close()

            return user
        
    # SELECIONAR CONTATO POR EMAIL   
    @classmethod
    def select_data_contato_email(cls, email):
        conexao = obter_conexao()
        cursor = conexao.cursor(buffered=True)
        SELECT = 'SELECT * FROM tb_usuarios WHERE usu_email=%s'
        cursor.execute(SELECT, (email,))
        dados = cursor.fetchone()
        if dados:
            user = User(dados[1], dados[2], dados[3])
            user.id = dados[0]

            conexao.commit()
            cursor.close()

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
        cursor = conexao.cursor()
        DELETE = 'DELETE FROM tb_livros WHERE liv_id=%s'
        cursor.execute(DELETE, (id,))
        conexao.commit()

        cursor.close()
        conexao.close()

# DELETAR CONTATO
    @classmethod
    def delete_data_contato(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        DELETE = 'DELETE FROM tb_contatos WHERE con_id=%s'
        cursor.execute(DELETE, (id,))
        conexao.commit()

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
    def insert_data_livro(cls, titulo, genero, id):
        conexao = obter_conexao()
    
        cursor = conexao.cursor()
        INSERT = 'INSERT INTO tb_livros (liv_titulo, liv_genero, liv_usuarios_id) VALUES (%s, %s, %s)'
        cursor.execute(INSERT, (titulo, genero, id))
        conexao.commit()

        cursor.close()
        conexao.close()

# INSERIR CONTATO
    @classmethod
    def insert_data_contato(cls, nome, email, id):
        conexao = obter_conexao()
    
        cursor = conexao.cursor()
        INSERT = 'INSERT INTO tb_contatos (con_nome, con_email, con_usuarios_id) VALUES (%s, %s, %s)'
        cursor.execute(INSERT, (nome, email, id))
        conexao.commit()

        cursor.close()
        conexao.close()

    # INSERIR CONVERSA
    @classmethod
    def insert_data_conversa(cls, id_contato, id, conteudo):
        conexao = obter_conexao()
    
        cursor = conexao.cursor()
        INSERT = 'INSERT INTO tb_mensagens (msg_usuario_from, msg_usuario_to, msg_texto) VALUES (%s, %s, %s)'
        cursor.execute(INSERT, (id, id_contato, conteudo))
        conexao.commit()

        cursor.close()
        conexao.close()