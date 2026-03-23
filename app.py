import streamlit as st
import pandas as pd
import plotly_express as px

# 1. Leer los datos
car_data = pd.read_csv('vehicles_us.csv') 

st.header('Análisis de datos de vehículos')

# --- SECCIÓN DEL HISTOGRAMA ---
# Crear un botón
hist_button = st.button('Construir histograma')

if hist_button: # al hacer clic en el botón
    st.write('Creando un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN DEL GRÁFICO DE DISPERSIÓN ---
# Nota: Estas líneas NO deben tener espacios al inicio (deben estar al borde izquierdo)
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter: # si la casilla está marcada
    st.write('Visualizando la relación entre el millaje y el precio')
    # Crear gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)