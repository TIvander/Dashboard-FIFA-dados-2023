import streamlit as st
import random 
df_data = st.session_state["data"]

st.set_page_config(
    page_title="Players",
    page_icon="👾",
    layout="wide"
)

#Armazena a lista de clubes
clubes = df_data["Club"].value_counts().index

#Armazena um clube específico da seleção
clube = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[df_data["Club"] == clube]

players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

#randomiza um número para gerar uma imagem aleatoria do robohash
id = random.randint(1,100)
url = f"https://robohash.org/{id}?set=set2&size=180x180"


st.image(url)
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Clube:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"$ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"$ {player_stats['Wage(£)']:,}")
col3.metric(label="Clásula de rescisão", value=f"$ {player_stats['Release Clause(£)']:,}")