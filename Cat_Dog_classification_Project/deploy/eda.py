import streamlit as st
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
   page_title= 'CatDog',
   layout='wide',
   initial_sidebar_state='expanded'
)
#def run():
# membuat Tittle
st.title('Cat or Dog')

'''
website ini bertujuan untuk mengklasifikasi apakah foto tersebut anjing atau kucing
'''

st.markdown('---')
st.markdown('---')

st.subheader('countplot kucing dan anjing')

image = Image.open('coutplot_catdog.png')
st.image(image, caption='counplot data latihan')

st.write('terlihat terdapat 4000 data kucing dan 4000 data anjing sebagai latihan computer vision kali ini')

st.markdown('---')

st.subheader('kdeplot ukuran gambar anjing dan kucing')
image = Image.open('kdeplot_catdog.png')
st.image(image, caption='kde plot data ukuran gambar latihan')

st.write('terlihat dari intensitasnya, foto dengan tinggi 500-550 pixel dan lebar 350-400 pixel merupakan ukuran ter-*mainstream* bagi penyimpan foto anjing dan kucing')

st.markdown('---')

#if __name__== '__main__':
#run()