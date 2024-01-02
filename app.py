import streamlit as st
import pandas as pd
dados = {
    'Nome': ['João', 'Maria', 'Carlos', 'Ana'],
    'Idade': [25, 30, 22, 28],
    'Salário': [5000, 6000, 4500, 5500]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

st.write(df)
st.write("Atualização 1")