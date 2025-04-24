import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título del dashboard
st.title('Dashboard 📊')

# Leer CSV
df = pd.read_csv('datasets_ventas.csv')

# Mostrar los datos
st.write(df)

# Gráfico simple
fig, ax = plt.subplots()
ax.bar(df['categoria'], df['precio_unitario'])
st.pyplot(fig)
