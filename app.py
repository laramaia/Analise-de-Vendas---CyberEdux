import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vgsales.csv")

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

st.write("") 

tab1, tab2, tab3, tab4 = st.tabs(["Top Jogos", "Distribuição Regional", "Distribuição por Gênero", "Tendências Temporais"])

# Top Jogos
with tab1:
    st.header("Top Jogos por Vendas")
    
    with st.sidebar:
        st.header("Filtros - Top Jogos")
        qtd = st.selectbox("Deseja exibir dados de quantos jogos?", [5, 10, 20])
        plataformas = df['Platform'].unique()
        opcoes = st.multiselect("Melhores jogos por plataforma", plataformas)
    
    df_top_jogos = df.groupby("Name")["Global_Sales"].sum()
    top_n_jogos = df_top_jogos.sort_values(ascending=False).head(qtd)
    
    fig = px.bar(top_n_jogos, x=top_n_jogos.values, y=top_n_jogos.index, orientation='h')
    st.plotly_chart(fig)

    plataformas_selecionadas = df[df['Platform'].isin(opcoes)]
    st.dataframe(plataformas_selecionadas)

# Distribuição Regional
with tab2:
    st.header("Distribuição de Vendas por Região")

    df["Decada"] = (df['Year'] // 10) * 10
    with st.sidebar:
        st.header("Filtros - Distribuição Regional")
        tipo_grafico = st.selectbox("Tipo de gráfico", ["Pizza", "Treemap"])
        decada = st.selectbox("Pesquisar por década", sorted(df["Decada"].unique()))
    
    df_venda_decada = df.groupby("Decada")[["Other_Sales", "JP_Sales", "EU_Sales", "NA_Sales"]].sum()
    vendas_regiao = df_venda_decada.loc[decada] # localiza linha da década selecionada

    df_venda_pais = pd.DataFrame({
        "regiao": ["Outras Vendas", "Japão", "Europa", "América do Norte"],
        "vendas_regiao": vendas_regiao.values # valor correspondente ao da década selecionada
    })

    if tipo_grafico == "Pizza":
        fig = px.pie(df_venda_pais, names="regiao", values="vendas_regiao", width=500, height=500)
    else:
        fig = px.treemap(df_venda_pais, path=["regiao"], values="vendas_regiao")

    st.plotly_chart(fig)

# Distribuição por Gênero
with tab3:
    st.header("Distribuição de Vendas por Gênero")
    df_vendas_por_genero = df.groupby("Genre")["Global_Sales"].sum().reset_index()
    fig = px.bar(df_vendas_por_genero, x="Global_Sales", y="Genre", orientation='h')
    st.plotly_chart(fig)

# Tendências Temporais
with tab4:
    st.header("Tendências Temporais de Vendas")
    df_tendencias_temporais = df.groupby("Year")["Global_Sales"].sum().reset_index()
    fig = px.bar(df_tendencias_temporais, x="Global_Sales", y="Year", orientation='h')
    st.plotly_chart(fig)