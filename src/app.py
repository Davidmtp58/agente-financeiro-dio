import streamlit as st
import google.generativeai as genai
import pandas as pd
import json
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

with open("data/perfil_investidor.json", "r", encoding="utf-8") as f:
    perfil = json.load(f)

with open("data/produtos_financeiros.json", "r", encoding="utf-8") as f:
    produtos = json.load(f)

transacoes = pd.read_csv("data/transacoes.csv")

st.title("BIA - Assistente Financeira")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    prompt = f"""
    Você é uma assistente financeira virtual.

    Responda em português do Brasil, de forma clara, simples e objetiva.

    Dados do cliente:
    {json.dumps(perfil, ensure_ascii=False, indent=2)}

    Produtos financeiros:
    {json.dumps(produtos, ensure_ascii=False, indent=2)}

    Histórico de transações:
    {transacoes.to_string(index=False)}

    Pergunta do usuário:
    {pergunta}
    """

    model = genai.GenerativeModel("gemini-3-flash-preview")
    resposta = model.generate_content(prompt)

    st.subheader("Resposta da BIA:")
    st.write(resposta.text)