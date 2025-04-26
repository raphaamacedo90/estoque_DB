USE estoque;

CREATE VIEW vw_vendas_total AS
SELECT 
    p.id AS produto_id,
    p.nome AS nome_produto,
    SUM(v.quantidade) AS total_vendido,
    SUM(v.quantidade * p.preco) AS valor_total
FROM produtos p
LEFT JOIN vendas v ON p.id = v.produto_id
GROUP BY p.id, p.nome;