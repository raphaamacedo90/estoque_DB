# Banco de Dados de Estoque

## 📘 Descrição
Este projeto é um sistema de gerenciamento de estoque desenvolvido com MySQL, criado como parte de um plano de estudos voltado para práticas reais de mercado.

O objetivo é praticar:
- Criação de tabelas e relacionamentos
- Views e consultas SQL otimizadas
- Inserção de dados manual e automatizada
- Organização de projeto e boas práticas para GitHub

---

## 🗂️ Estrutura do Projeto

estoque-projeto/  
├── dados/                # Arquivos de dados em CSV  
├── sql/  
│   ├── criar_tabelas.sql     # Criação das tabelas produtos e vendas  
│   ├── criar_view.sql        # Criação da view vw_vendas_total  
│   ├── inserir_dados.sql     # Inserção manual de dados com SQL  
│   └── consultas.sql         # Consultas úteis (ex.: estoque baixo)  
├── scripts/  
│   └── inserir_dados.py      # Script Python para inserir dados a partir dos CSVs  
├── relatorios/           # Relatórios gerados <br>
├── dashboard/           # Dashboard Criado<br>
└── README.md             # Documentação do projeto

---

## ✅ Progresso Atual 
- Banco de dados `estoque` criado no MySQL.
- Tabelas `produtos` e `vendas` criadas (`criar_tabelas.sql`).
- View `vw_vendas_total` criada (`criar_view.sql`).
- Estrutura de diretórios organizada.
- Dados simulados prontos para inserção.

---

## 🔁 Inserção de Dados

A inserção pode ser feita de duas formas, para simular diferentes cenários usados no mercado:

### 1. Manual (via SQL)
- Arquivo: `sql/inserir_dados.sql`
- Executar diretamente no MySQL ou via SQLTools (VS Code)

### 2. Automática (via Python)
- Script: `scripts/inserir_dados.py`
- Lê os arquivos `produtos.csv` e `vendas.csv` da pasta `dados/`
- Insere os dados no banco `estoque` automaticamente


---

## 📌 Consultas
- A view `vw_vendas_total` permite ver o valor total de cada venda.
- Consultas adicionais para estoque baixo e agrupamentos em `consultas.sql`.

---

## 🐛 Simulação de Bug
- O projeto inclui uma etapa para simular e corrigir bugs comuns, como inserção com `produto_id` inválido.
- Isso ajuda a reforçar a habilidade de resolver problemas reais de banco de dados.

---

## 🚀 Novidades do Projeto

Finalizei também um dashboard em Power BI conectado ao banco de dados, trazendo:
- Visão de vendas por mês
- Ranking dos produtos mais vendidos
- Indicadores de desempenho

O arquivo `.pbix` está disponível na pasta `/dashboard`.

📊 O objetivo foi construir uma jornada completa: dados → análise → visualização!

# Projeto de Estoque - Banco de Dados + Dashboard Power BI

Este projeto foi desenvolvido em etapas para treinar habilidades práticas em Banco de Dados, Python e Power BI.

## Etapas do Projeto:
- **Criação do Banco de Dados**: Estruturado com tabelas de produtos e vendas.
- **Script em Python**: Planejado para futuras automações de análise.
- **Dashboard no Power BI**: Desenvolvimento de um dashboard dinâmico de vendas.

## O que foi feito:
- Estruturação de um banco de dados relacional para simular um ambiente real de estoque e vendas.
- Desenvolvimento de um Dashboard em Power BI conectado diretamente ao banco de dados para análise interativa.
- Integração de indicadores, filtros e ranking dos produtos mais vendidos.


---

📊 Este projeto representa a jornada prática de um banco de dados até a visualização dos dados em um dashboard.

👨‍💻 Projeto por Raphael Macedo  
[https://app.powerbi.com/view?r=eyJrIjoiZDcxZDY1OWYtN2NiNS00MWY1LWJmMjQtNThmNjY5ZWZkZDIxIiwidCI6ImJhNjE3ZWIyLWRiZDYtNGY2YS04ODJjLWQ2OGY5MzgwOGEzZiJ9]



## ▶️ Como Executar

1. Configure um servidor MySQL local (ex.: XAMPP, WAMP ou Docker).
2. Crie o banco de dados:
   ```sql
   CREATE DATABASE estoque;
   USE estoque;

3. Execute os arquivos em `sql/` para criar tabelas, views e inserir dados (opcional).  
4. Execute o script Python se desejar automatizar a inserção:

```bash
pip install pandas pymysql
python scripts/inserir_dados.py
```
--- 

🛠️ Tecnologias Utilizadas
- MySQL

- Python (pandas, pymysql)

- Visual Studio Code 
  
- Power BI Desktop

- Git e GitHub

--- 

📬 Contato
- GitHub: github.com/raphaamacedo90/estoque_DB

- LinkedIn: linkedin.com/in/raphael-macedo10


















