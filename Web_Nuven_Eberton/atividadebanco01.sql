CREATE TABLE  empresa(
  cnpj varchar(20) NOT NULL,
  inscricao_estadual varchar(20) NOT NULL,
  razao_social varchar(200) NOT NULL,
  nome_fantasia varchar(200) NOT NULL,
  end_logradouro varchar(200) NOT NULL,
  end_numero int NOT NULL,
  end_bairro varchar(200) NOT NULL,
  end_cidade varchar(200) NOT NULL,
  end_estado varchar(200) NOT NULL,
  end_cep varchar(10) NOT NULL,
  PRIMARY KEY (cnpj)
);

INSERT INTO empresa (cnpj,inscricao_estadual,razao_social,nome_fantasia,end_logradouro,end_numero,end_bairro,end_cidade,end_estado,end_cep) VALUES 
 ('123455677/89','123456','F Souza Sousa','F Souza Sousa','Casa','10','Centro','Goianinha','RN','5917300');

select * from empresa;

CREATE TABLE funcionario (
  cpf varchar(20) NOT NULL,
  nome varchar(200) NOT NULL,
  rg varchar(20) NOT NULL,
  Sexo varchar(10) NOT NULL,
  data_nascimento date NOT NULL,
  end_logradouro varchar(200) NOT NULL,
  end_numero int NOT NULL,
  end_cidade varchar(200) NOT NULL,
  end_bairro varchar(200) NOT NULL,
  end_estado varchar(200) NOT NULL,
  end_cep varchar(10) NOT NULL,
  data_admissao date NOT NULL,
  n_carteira_trabalho varchar(45) NOT NULL,
  PRIMARY KEY (cpf)
);

CREATE TABLE produto (
  idproduto int NOT NULL IDENTITY(1,1),
  nome varchar(100) NOT NULL,
  descricao varchar(300) NOT NULL,
  unidade varchar(45) NOT NULL,
  preco_unitario float NOT NULL,
  PRIMARY KEY (idproduto)
);

CREATE TABLE caixa (
  idCaixa int NOT NULL IDENTITY(1,1),
  descricao varchar(300) NOT NULL,
  PRIMARY KEY (idCaixa)
);

CREATE TABLE funcionario_caixa (
  idfuncionario_caixa int NOT NULL IDENTITY(1, 1),
  fk_funcionario_cpf varchar(20) NOT NULL,
  fk_idCaixa int NOT NULL,
  data_abertura date NOT NULL,
  hora_abertura time NOT NULL,
  valor_abertura float NOT NULL,
  data_fechamento date NOT NULL,
  hora_fechamento time NOT NULL,
  valor_fechamento float NOT NULL,
  diferenca float NOT NULL,
  situacao varchar(30) NOT NULL,
  PRIMARY KEY (idfuncionario_caixa),
  FOREIGN KEY (fk_funcionario_cpf) REFERENCES funcionario (cpf),
  FOREIGN KEY (fk_idCaixa) REFERENCES caixa (idCaixa) 
) ;

CREATE TABLE cupom_fiscal (
  ccf int NOT NULL IDENTITY(1, 1),
  data date NOT NULL,
  hora time NOT NULL,
  valor_total float NOT NULL,
  fk_empresa_cnpj varchar(20) NOT NULL,
  fk_funcionario_caixa_idfuncionario_caixa int NOT NULL,
  PRIMARY KEY (ccf),
  FOREIGN KEY (fk_empresa_cnpj) REFERENCES empresa (cnpj),
  FOREIGN KEY (fk_funcionario_caixa_idfuncionario_caixa) REFERENCES funcionario_caixa (idfuncionario_caixa)
);

CREATE TABLE item_cupom_fiscal (
  fk_cumpo_fiscal_ccf int NOT NULL IDENTITY(1, 1),
  fk_produto_idproduto int NOT NULL,
  item int NOT NULL,
  qtd varchar(45) NOT NULL,
  valor_item varchar(45) NOT NULL,
  PRIMARY KEY (fk_cumpo_fiscal_ccf,fk_produto_idproduto,item),
  FOREIGN KEY (fk_cumpo_fiscal_ccf) REFERENCES cupom_fiscal (ccf),
  FOREIGN KEY (fk_produto_idproduto) REFERENCES produto (idproduto) 
) ;