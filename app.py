import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Análise de anúncios de vendas de veículos nos Estados Unidos")

st.subheader("Selecione sua opção:", divider='red')

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Histograma para o conjunto de dados de anúncios de veículos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.button('Criar gráfico de dispersão')
if build_histogram:
    st.write('Gráfico de dispersão:')
    fig = px.scatter(car_data, x="odometer", y="price") 
    st.plotly_chart(fig, use_container_width=True)
    

build_checkbox = st.checkbox('Criando um histograma:')
if build_checkbox:
    st.write('Histograma:')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

build_checkbox = st.checkbox('Criando um gráfico de dispersão:')
if build_checkbox:
    st.write('Gráfico de dispersão:')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)