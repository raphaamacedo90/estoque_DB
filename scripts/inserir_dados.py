import pandas as pd
import mysql.connector
from mysql.connector import Error

print("Iniciando o script...")

try:
    print("Tentando conectar ao MySQL...")
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R@phael10!",
        database="Estoque",
        port=3306
    )

    print("Conexão criada, verificando status...")
    if conn.is_connected():
        print("Conexão com MySQL estabelecida!")
    else:
        print("Falha na conexão com MySQL!")
    
    cursor = conn.cursor()

    print("Lendo produtos.csv...")
    produtos_df = pd.read_csv("../dados/produtos.csv")
    print("Produtos lido com sucesso!")

    produtos_data = [
        (
            row["nome"],
            row["descricao"],
            float(row["preco"]),
            int(row["quantidade"]),
            row["categoria"]
        )
        for _, row in produtos_df.iterrows()
    ]

    sql_produtos = """
    INSERT INTO produtos (nome, descricao, preco, quantidade, categoria)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.executemany(sql_produtos, produtos_data)
    print(f"{cursor.rowcount} registros inseridos na tabela produtos.")
    conn.commit()

    cursor.execute("SELECT id FROM produtos")
    valid_produto_ids = {row[0] for row in cursor.fetchall()}
    print(f"IDs válidos de produtos: {valid_produto_ids}")

    print("Lendo vendas.csv...")
    vendas_df = pd.read_csv("../dados/vendas.csv")
    print("Vendas lido com sucesso!")

    vendas_data = []
    for _, row in vendas_df.iterrows():
        produto_id = int(row["produto_id"])
        if produto_id not in valid_produto_ids:
            print(f"Aviso: produto_id {produto_id} não existe. Linha ignorada.")
            continue
        vendas_data.append(
            (
                produto_id,
                pd.to_datetime(row["data_venda"]).strftime("%Y-%m-%d"),
                int(row["quantidade"])
            )
        )

    sql_vendas = """
    INSERT INTO vendas (produto_id, data_venda, quantidade)
    VALUES (%s, %s, %s)
    """
    cursor.executemany(sql_vendas, vendas_data)
    print(f"{cursor.rowcount} registros inseridos na tabela vendas.")
    conn.commit()
    print("Dados importados com sucesso!")

except Error as e:
    print(f"Erro ao importar os dados: {e}")
    if conn.is_connected():
        conn.rollback()

except pd.errors.EmptyDataError as ede:
    print(f"Erro: CSV vazio ou inválido: {ede}")

except ValueError as ve:
    print(f"Erro de conversão de tipos: {ve}")

except Exception as ex:
    print(f"Erro inesperado: {ex}")
    raise

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão com MySQL fechada.")