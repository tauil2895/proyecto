import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')


hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # es cribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    hist = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(hist, use_container_width=True)

scatter_button = st.button('Construir grafico de dispersion') # crear un botón
        
if scatter_button: # al hacer clic en el botón
    # es cribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    scatter = px.scatter(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(scatter, use_container_width=True)