import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir una gráfica de dispersión')

st.header ('PROYECTO SPRINT 7:')
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Histograma para el conjunto de datos de anuncios de venta de coches en EUA')
         
# crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Gráfico de dispersión para anuncios y precio')
         
# crear un histograma
    fig_2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)