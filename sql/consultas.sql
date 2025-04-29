#Consulta 1: Listar todos os produtos
SELECT id, nome, preco, quantidade, categoria, descricao
FROM produtos;

#Consulta 2: Total de vendas por produto
SELECT produto_id, nome_produto, total_vendido, valor_total
FROM vw_vendas_total;

#Consulta 3: Produtos com estoque baixo
SELECT nome, quantidade
FROM produtos
WHERE quantidade < 50;

#Consulta 4: Valor total de vendas
SELECT 
   p.nome AS produto,
   SUM(v.quantidade * p.preco) AS valor_total
FROM vendas v
JOIN produtos p ON v.produto_id = p.id
WHERE v.data_venda BETWEEN '2025-04-01' AND '2025-04-30'
GROUP BY p.nome
ORDER BY valor_total DESC;


