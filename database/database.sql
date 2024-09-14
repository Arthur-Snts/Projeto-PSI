CREATE DATABASE IF NOT EXISTS romerito_database;
USE romerito_database;

CREATE TABLE IF NOT EXISTS tb_usuarios (
    usu_id INT(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    usu_nome VARCHAR(200) NOT NULL,
    usu_email VARCHAR(200) NOT NULL,
    usu_senha VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_contatos (
    con_id INT(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    con_email VARCHAR(200) NOT NULL,
    con_usuarios_id INT(11) NOT NULL,
    FOREIGN KEY (con_usuarios_id) REFERENCES tb_usuarios(usu_id)
);

CREATE TABLE IF NOT EXISTS tb_livros (
    liv_id INT(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    liv_titulo VARCHAR(200) NOT NULL,
    liv_genero VARCHAR(200) NOT NULL,
    liv_usuarios_id INT(11) NOT NULL,
    FOREIGN KEY (liv_usuarios_id) REFERENCES tb_usuarios(usu_id)
);

CREATE TABLE IF NOT EXISTS tb_mensagens (
    msg_id INT AUTO_INCREMENT PRIMARY KEY,
    msg_usuario_from INT NOT NULL,
    msg_usuario_to INT NOT NULL,
    msg_texto TEXT NOT NULL,
    msg_data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (msg_usuario_from) REFERENCES tb_usuarios(usu_id) ON DELETE CASCADE,
    FOREIGN KEY (msg_usuario_to) REFERENCES tb_usuarios(usu_id) ON DELETE CASCADE
);
