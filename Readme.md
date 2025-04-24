# Banco de Dados de Estoque

## Descrição
Este projeto é um sistema de gerenciamento de estoque desenvolvido com MySQL, criado como parte do plano de estudos de TI (Mês 3, Semana 1). O objetivo é praticar conceitos de banco de dados relacionais, incluindo criação de tabelas, views, inserção de dados, consultas e resolução de bugs.

O sistema gerencia produtos e vendas, com funcionalidades para consultar estoque baixo e gerar relatórios básicos.

## Estrutura do Projeto

estoque-projeto/
├── dados/ # Arquivos de dados (ex.: exportações em CSV, backups)
├── sql/ # Scripts SQL
│ ├── criar_tabelas.sql # Criação das tabelas produtos e vendas
│ ├── criar_view.sql # Criação da view vw_vendas_total
│ ├── inserir_dados.sql # Inserção de dados fictícios
│ └── consultas.sql # Consultas SQL (ex.: estoque baixo)
├── scripts/ # Scripts adicionais (futuro)
├── relatorios/ # Relatórios gerados (futuro)
└── README.md # Documentação do projeto


## Progresso Atual 
- **Dia 1: Configuração Inicial**
  - Banco de dados `estoque` criado no MySQL.
  - Tabelas `produtos` e `vendas` criadas (`criar_tabelas.sql`).
  - View `vw_vendas_total` criada para calcular o total das vendas (`criar_view.sql`).
  - Estrutura do projeto.

## Próximos Passos
- **Inserção de Dados**
  - Inserir dados fictícios nas tabelas `produtos` e `vendas` (`inserir_dados.sql`).
  - Testar a view `vw_vendas_total` com os dados inseridos.
- **Consultas**
  - Criar uma consulta para identificar produtos com estoque baixo (`consultas.sql`).

- **Bugfix**
  - Simular e corrigir um bug (ex.: inserção de venda com `produto_id` inválido).
  - A simulação irá me proporcionar o dia a dia de trabalho para que eu possa saber lidar com os problemas e resolver de maneira rápida e eficiente.

## Tecnologias Utilizadas
MySQL
Código VS (com extensão SQLTools)
Git/GitHub

## Contato
Repositório: github.com/raphaamacedo90/estoque_DB
LinkedIn: https://www.linkedin.com/in/raphael-macedo10
"# estoque_DB" 
