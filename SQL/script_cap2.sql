-- Criação do schema do capitulo 2
CREATE SCHEMA `cap02` ;

USE cap02;

CREATE TABLE tb_navios
(
	nome_navio VARCHAR(50),
    mes_ano VARCHAR(10),
    classificacao_risco VARCHAR(15),
    indice_conformidade VARCHAR(15),
    pontuacao_risco INT,
    temporada VARCHAR(200)
);

SELECT nome_navio, mes_ano FROM cap02.tb_navios;

