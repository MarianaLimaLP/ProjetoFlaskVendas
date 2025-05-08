DROP DATABASE IF EXISTS loja;

CREATE DATABASE loja;
USE loja;

CREATE TABLE cliente (
    codcliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200)
);

CREATE TABLE produto (
    codproduto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL
);

CREATE TABLE venda (
    codvenda INT PRIMARY KEY AUTO_INCREMENT,
    data DATE NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    codcliente INT,
    FOREIGN KEY (codcliente) REFERENCES Cliente(codcliente)
);

CREATE TABLE itemvenda (
    codvenda INT,
    codproduto INT,
    qtde INT NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (codvenda, codproduto),
    FOREIGN KEY (codvenda) REFERENCES Venda(codvenda),
    FOREIGN KEY (codproduto) REFERENCES Produto(codproduto)
);
