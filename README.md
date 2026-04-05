# BIA - Assistente Financeira

Projeto desenvolvido como atividade do bootcamp DIO, com foco em Inteligência Artificial generativa aplicada ao relacionamento financeiro.

## Sobre o projeto

A **BIA - Assistente Financeira** é uma aplicação simples desenvolvida em **Python** com **Streamlit**, que utiliza IA generativa para responder perguntas financeiras com base em dados do perfil do usuário, produtos financeiros disponíveis e histórico de transações.

A proposta do projeto é simular uma experiência digital voltada ao apoio financeiro, oferecendo respostas contextualizadas de forma clara, simples e personalizada.

## Objetivo

Criar uma assistente virtual capaz de:

- responder dúvidas financeiras
- analisar informações do perfil do usuário
- considerar produtos financeiros disponíveis
- utilizar dados de transações para gerar respostas mais contextualizadas
- demonstrar o uso de IA generativa em uma aplicação prática

## Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- Google Generative AI
- JSON
- CSV
- python-dotenv

## Estrutura do projeto

```bash
agente-financeiro-dio/
│
├── data/
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   └── transacoes.csv
│
├── src/
│   └── app.py
│
├── .gitignore
└── README.md
