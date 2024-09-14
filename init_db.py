# Importing MySQL connector
import mysql.connector

db_config = {
    'user': 'root',
    'password': 'h4rdr00tp4sw#rd',
    'host': 'localhost',
    'port': 3306,
}
try:
    # Tentando estabelecer uma conexão
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
except mysql.connector.Error as erro:
    print(f"Erro ao conectar ou criar banco de dados: {erro}")
finally:
    conn.close()


# Abre conexão
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Localização do sql
SCHEMA = "database/database.sql"

# Declara o sql para o banco
with open(SCHEMA, 'r') as f:
    sql_script = f.read()

for statement in sql_script.split(';'):
    if statement.strip():
        try:
            cursor.execute(statement)
        except mysql.connector.Error as e:
            print(f"Erro ao executar statement: {e}")

# Encerra operações
conn.commit()
cursor.close()
conn.close()