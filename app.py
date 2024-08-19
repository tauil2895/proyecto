import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')


select_button = st.selectbox('Construir un histograma', ('Seleccionar', 'Histograma', 'Dispersion')) # crear un botón
        
if select_button=='Histograma': # al hacer clic en el botón
    # es cribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    hist = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(hist, use_container_width=True)

        
if select_button=='Dispersion': # al hacer clic en el botón
    # es cribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    scatter = px.scatter(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(scatter, use_container_width=True)