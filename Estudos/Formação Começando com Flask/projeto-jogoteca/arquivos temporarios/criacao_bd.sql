CREATE DATABASE jogoteca;

USE jogoteca;

CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    login_user VARCHAR(100) NOT NULL,
    senha_user VARCHAR(100) NOT NULL
);

CREATE TABLE jogos (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    console VARCHAR(100) NOT NULL
);


-- INSERÇÃO DE DADOS (esses dados vão ser inseridos pelo python também)
INSERT INTO usuarios (nome, login_user, senha_user) VALUES 
    ('Luan Marques', 'luan', '1234'),
    ('Marcos Vinicius', 'marquinho', '4321'),
    ('Danilo Silva', 'danilo', 'vegas12');

INSERT INTO jogos (nome, categoria, console) VALUES
    ('God of War 2', 'Ação', 'PS3'),
    ('Devil May Cry 4', 'Rogue Like', 'PS4'),
    ('Minecraft', 'Aventura', 'PC');



SELECT * FROM jogos;
/*
+----+-----------------+------------+---------+
| id | nome            | categoria  | console |
+----+-----------------+------------+---------+
|  1 | God of War 2    | Ação       | PS3     |
|  2 | Devil May Cry 4 | Rogue Like | PS4     |
|  3 | Minecraft       | Aventura   | PC      |
+----+-----------------+------------+---------+
*/

SELECT * FROM usuarios;
/*
+----+-----------------+------------+------------+
| id | nome            | login_user | senha_user |
+----+-----------------+------------+------------+
|  1 | Luan Marques    | luan       | 1234       |
|  2 | Marcos Vinicius | marquinho  | 4321       |
|  3 | Danilo Silva    | danilo     | vegas12    |
+----+-----------------+------------+------------+
*/