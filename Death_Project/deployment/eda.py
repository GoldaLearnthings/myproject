import streamlit as st
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
   page_title= 'gagal jantung?',
   layout='wide',
   initial_sidebar_state='expanded'
)

def run():
    # membuat Tittle
    st.title('prediksi pasien gagal jantung')

    # magic syntax
    '''
    pada page kali ini, penulis akan mencoba jampi-jampi jantung anda
    '''

    # show dataframe
    data = pd.read_csv('h8dsft_P1G3_golda.csv')
    st.dataframe(data)

    # membuat barplot
    st.write('#### plot untuk diabetes')
    fig = plt.figure(figsize= (15,5))
    sns.countplot(x= 'diabetes', data=data)
    st.pyplot(fig)

    # membuat histogram
    st.write('#### histogram of platelets')
    fig = plt.figure(figsize= (15,5))
    sns.histplot(data['platelets'], bins=30, kde=True)
    st.pyplot(fig)

    st.write('#### histogram of creatinine_phosphokinase')
    fig = plt.figure(figsize= (15,5))
    sns.histplot(data['creatinine_phosphokinase'], bins=30, kde=True)
    st.pyplot(fig)

    st.write('#### histogram of serum_sodium')
    fig = plt.figure(figsize= (15,5))
    sns.histplot(data['serum_sodium'], bins=30, kde=True)
    st.pyplot(fig)

    # membuat plotly plot
    st.write('#### Plotly Plot - serum kreatinin dengan serum sodium')
    fig = px.scatter(data, x='serum_creatinine', y= 'serum_sodium', hover_data=['DEATH_EVENT', 'age'])
    st.plotly_chart(fig)

    # membuat histogram berdasarkan input user
    st.write('#### Histogram berdasarkan Input user')
    pilihan = st.selectbox('pilih colomn: ', ('platelets', 'ejection_fraction', 'age'))
    fig = plt.figure(figsize= (15,5))
    sns.histplot(data[pilihan], bins=30, kde=True)
    st.pyplot(fig)

if __name__== '__main__':
    run()