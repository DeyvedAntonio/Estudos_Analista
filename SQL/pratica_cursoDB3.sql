CREATE DATABASE curso_sql;

USE curso_sql;

CREATE TABLE funcionarios
(
   id INT UNSIGNED NOT NULL AUTO_INCREMENT,
   nome VARCHAR(45) NOT NULL,
   salario DOUBLE NOT NULL DEFAULT '0',
   departamento VARCHAR(45) NOT NULL,
   PRIMARY KEY (id)
);

CREATE TABLE veiculos
(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    funcionario_id INT UNSIGNED DEFAULT NULL,
    veiculo VARCHAR(45) NOT NULL DEFAULT '',
    placa VARCHAR(10) NOT NULL DEFAULT '',
    PRIMARY KEY(id),
    CONSTRAINT fk_veiculo_funcionario FOREIGN KEY (funcionario_id) REFERENCES funcionarioS(id)
);

CREATE TABLE salarios
(
	faixa VARCHAR(45) NOT NULL,
    inicio DOUBLE NOT NULL,
    fim DOUBLE NOT NULL,
    PRIMARY KEY(faixa)
);

ALTER TABLE funcionarios CHANGE COLUMN nome nome_func VARCHAR(50) NOT NULL;

DROP TABLE salarios;

CREATE INDEX departamentos ON funcionarios(departamento);