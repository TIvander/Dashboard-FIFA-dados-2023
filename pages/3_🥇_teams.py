import random
import streamlit as st

id = random.randint(1,100)
url = f"https://robohash.org/{id}?set=set2&size=20x20"
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
df_filtered = df_data[df_data["Club"] == clube].set_index("Name")
st.markdown(f"## 👽 {clube}")

columns = ["Age", "Photo", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

df_filtered["Photo"] = df_filtered["Photo"].apply(lambda x: f"https://robohash.org/{random.randint(1,100)}?set=set2&size=90x100")

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn(
                     "Weekly Wage", min_value=0, max_value=df_filtered["Wage(£)"].max(), format="%d"
                 ),
                 "Photo": st.column_config.ImageColumn("Photo")
             })