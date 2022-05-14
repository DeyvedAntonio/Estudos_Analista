CREATE SCHEMA `cap02` ;

CREATE TABLE `cap03`.`TB_DADOS` (
  `classe` VARCHAR(100) NULL,
  `idade` VARCHAR(45) NULL,
  `menopausa` VARCHAR(45) NULL,
  `tamanho_tumor` VARCHAR(45) NULL,
  `inv_nodes` VARCHAR(45) NULL,
  `node_caps` VARCHAR(3) NULL,
  `deg_malig` INT NULL,
  `seio` VARCHAR(5) NULL,
  `quadrante` VARCHAR(10) NULL,
  `irradiando` VARCHAR(3) NULL);
  
SELECT DISTINCT irradiando FROM cap03.tb_dados;  

SELECT
	CASE
		WHEN irradiando = 'no' THEN 0
        ELSE 1
	END AS irradiando
FROM cap03.tb_dados;

SELECT DISTINCT node_caps FROM cap03.tb_dados;

SELECT
	CASE
		WHEN node_caps = 'no' THEN 0
        WHEN node_caps = 'yes' THEN 1
        ELSE NULL
	END AS node_caps
FROM cap03.tb_dados;