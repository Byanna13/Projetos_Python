CREATE TABLE clientes (
  idCliente int NOT NULL IDENTITY(1,1),
  nome varchar(100) NOT NULL,
  dataNascimento date NOT NULL,
  Sexo char(1) NOT NULL,
  CPF varchar(11) NOT NULL,
  endereco varchar(200) NOT NULL,
  PRIMARY KEY (idCliente)
);

INSERT INTO clientes (nome,dataNascimento,Sexo,CPF,endereco) VALUES 
 ('Maria Joaquina de Amaral Pereira Goes','1996-06-26','F','12345567789','Rua Salvador Dali');

select * from clientes;

CREATE TABLE produtos (
  codProduto int NOT NULL IDENTITY(1,1),
  descricao varchar(200) NOT NULL,
  unidade varchar(10) NOT NULL,
  vlUnitario float NOT NULL,
  PRIMARY KEY (codProduto)
);

CREATE TABLE cuponsfiscais (
  ccf int NOT NULL IDENTITY(1, 1),
  data date NOT NULL,
  hora time NOT NULL,
  formaPagamento int NOT NULL,
  vlTotal float NOT NULL,
  fk_idCliente int NOT NULL,
  PRIMARY KEY (ccf),
  FOREIGN KEY (fk_idCliente) REFERENCES clientes (idCliente),
);

CREATE TABLE itemcupom (
  fk_ccf int NOT NULL IDENTITY(1, 1),
  fk_codProduto int NOT NULL,
  fk_nItem int NOT NULL,
  qtd int NOT NULL,
  vlItem float NOT NULL,
  PRIMARY KEY (fk_ccf,fk_codProduto,fk_nItem),
  FOREIGN KEY (fk_ccf) REFERENCES cuponsfiscais (ccf),
  FOREIGN KEY (fk_codProduto) REFERENCES produtos (codProduto) 
) ;