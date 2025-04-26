USE estoque;

CREATE TABLE produtos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    quantidade INT NOT NULL,
    categoria VARCHAR(50),
    descricao TEXT
);

CREATE TABLE vendas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    produto_id INT,
    data_venda DATE,
    quantidade INT,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);