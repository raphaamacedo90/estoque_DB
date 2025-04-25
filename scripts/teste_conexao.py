print("Iniciando teste...")

try:
    import mysql.connector
    print("Biblioteca mysql-connector-python importada com sucesso!")
    
    print("Tentando conectar ao MySQL...")
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R@phael10!",
        database="estoque",
        port=3306
    )
    print("Conexão criada, verificando status...")
    if conn.is_connected():
        print("Conexão bem-sucedida!")
    else:
        print("Conexão falhou!")
except mysql.connector.Error as e:
    print(f"Erro MySQL: {e}")
except Exception as e:
    print(f"Erro inesperado: {type(e).__name__}: {e}")
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Conexão fechada.")