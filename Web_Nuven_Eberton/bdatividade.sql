CREATE TABLE  empresa(
  cnpj varchar(20) NOT NULL IDENTITY(1,1),
  inscricao_esta varchar(20) NOT NULL,
  razao_social varchar(100) NOT NULL,
  nome_fantasia varchar(30) NOT NULL,
  end_logradouro varchar(40) NOT NULL,
  end_numero int NOT NULL,
  end_bairro varchar(40) NOT NULL,
  end_cidade varchar(40) NOT NULL,
  end_estado varchar(40) NOT NULL,
  end_cep varchar(40) NOT NULL,
  PRIMARY KEY (cnpj)
);

INSERT INTO clientes (nome,dataNascimento,Sexo,CPF,endereco) VALUES 
 ('Maria Joaquina de Amaral Pereira Goes','1996-06-26','F','12345567789','Rua Salvador Dali');

select * from empresa;

CREATE TABLE funcionario (
  cpf int NOT NULL IDENTITY(1,1),
  nome varchar(100) NOT NULL,
  rg varchar(30) NOT NULL,
  Sexo varchar(10) NOT NULL,
  dataNascimento date NOT NULL,
  end_logradouro varchar(200) NOT NULL,
  end_numero int NOT NULL,
  end_cidade varchar(40) NOT NULL,
  end_bairro varchar(40) NOT NULL,
  end_estado varchar(40) NOT NULL,
  end_cep varchar(40) NOT NULL,
  data_admissao date NOT NULL,
  n_carteira_trabalho varchar(35) NOT NULL,
  PRIMARY KEY (cpf)
);

CREATE TABLE produto (
  idProduto int NOT NULL IDENTITY(1,1),
  nome varchar(100) NOT NULL,
  descricao varchar(200) NOT NULL,
  unidade varchar(45) NOT NULL,
  preco_unitario float NOT NULL,
  PRIMARY KEY (idProduto)
);

CREATE TABLE caixa (
  idCaixa int NOT NULL IDENTITY(1,1),
  descricao varchar(100) NOT NULL,
  PRIMARY KEY (idCaixa)
);

CREATE TABLE funcionario_caixa (
  idFuncionario_caixa int NOT NULL IDENTITY(1, 1),
  fk_funcionario_cpf varchar(30) NOT NULL,
  fk_idCaixa int NOT NULL,
  data_abertura date NOT NULL,
  vlItem float NOT NULL,
  PRIMARY KEY (fk_ccf,fk_codProduto,fk_nItem),
  FOREIGN KEY (fk_ccf) REFERENCES cuponsfiscais (ccf),
  FOREIGN KEY (fk_codProduto) REFERENCES produtos (codProduto) 
) ;

CREATE TABLE cupom_fiscal (
  ccf int NOT NULL IDENTITY(1, 1),
  data date NOT NULL,
  hora time NOT NULL,
  valor_total float NOT NULL,
  fk_empresa_cnpj int NOT NULL,
  fk_funcionario_caixa_idfuncionario_caixa int NOT NULL,
  PRIMARY KEY (ccf),
  FOREIGN KEY (fk_empresa_cnpj) REFERENCES empresa (cnpj),
  FOREIGN KEY (fk_funcionario_caixa_idfuncionario_caixa) REFERENCES funcionario (cpf)
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