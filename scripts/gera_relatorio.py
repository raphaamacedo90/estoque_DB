import mysql.connector
import pandas as pd
import datetime

def registrar_log(mensagem):
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S")
    with open("logs_execucao.txt", "a") as f:
        f.write(f"[{agora} {mensagem}\n")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="R@phael10!",
    database="estoque",
    port="3306"
)



consultas = {
    "lista_todos_produtos": {
        "query": "SELECT id, nome, preco, quantidade, categoria, descricao FROM produtos;",
        "arquivo": "../relatorios/lista_todos_produtos.csv"
    },
    "total_vendas_por_produto": {
        "query": "SELECT produto_id, nome_produto, total_vendido, valor_total FROM vw_vendas_total;",
        "arquivo": "../relatorios/total_vendas_por_produto.csv"
    },
    "produtos_estoque_baixo": {
        "query": "SELECT nome, quantidade FROM produtos WHERE quantidade < 50;",
        "arquivo": "../relatorios/produtos_estoque_baixo.csv"
    },
    "valor_total_vendas": {
    "query": """
        SELECT 
            p.nome AS produto, 
            SUM(v.quantidade * p.preco) AS valor_total
        FROM vendas v
        JOIN produtos p ON v.produto_id = p.id
        WHERE v.data_venda BETWEEN '2024-01-01' AND '2025-04-30'
        GROUP BY p.nome
        ORDER BY valor_total DESC;
    """,
    "arquivo": "../relatorios/valor_total_vendas.csv"
    }
}

print("Escolha o relatório para gerar: ")
for i, relatorio in enumerate(consultas.keys(), start = 1):
    print(f"{i}. {relatorio}")

opcao = int(input("Digite o número da opção desejada: "))  
relatorio_selecionado = list(consultas.keys()) [opcao - 1] 

query = consultas[relatorio_selecionado]["query"]
arquivo = consultas[relatorio_selecionado]["arquivo"]

try:
   df = pd.read_sql(query, conn)
   df.to_csv(arquivo, index=False)
   print("Relatório gerado com sucesso!")
   registrar_log(f"Relatório '{relatorio_selecionado}' gerado com sucesso e salvo em '{arquivo}'.")
except Exception as e:
    print("Erro ao gerar relatório:", e)
    registrar_log(f"Erro ao gerar relatório '{relatorio_selecionado}': {e}")   

conn.close()

print("Relatório gerado!")