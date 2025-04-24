import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("vgsales.csv")

st.title("Análise de Vendas")

st.header("Métricas Gerais")

col1, col2, col3 = st.columns(3)
with col1:
    st.write("Total de Jogos Únicos")
    total_jogos = df['Name'].nunique()
    st.write(total_jogos)
with col2:
    st.write("Ano do Jogo Mais Antigo")
    jogo_mais_antigo = df['Year'].min()
    st.write(jogo_mais_antigo)
with col3:
    st.write("Ano do Jogo Mais Recente")
    jogo_mais_recente = df['Year'].max()
    st.write(jogo_mais_recente)
    
col4, col5 = st.columns(2)   
with col4:
    st.write("Média Global de Vendas por Jogo")
    media_venda_por_jogo = df['Global_Sales'].mean()
    st.write(media_venda_por_jogo)

with col5:
    st.write("Editora com Maior Número de Jogos Publicados")
    editora_mais_publicada = df['Publisher'].value_counts().idxmax()
    st.write(editora_mais_publicada)

st.button("Top Jogos Por Venda")
st.button("Distribuição de Vendas Por Região")
st.button("Popularidade de Gêneros")
st.button("Tendências Temporais")
