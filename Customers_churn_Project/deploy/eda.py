import streamlit as st
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
   page_title= 'pelanggan pergi?',
   layout='wide',
   initial_sidebar_state='expanded'
)
def run():
    # membuat Tittle
    st.title('prediksi pelanggan yang tak akan kembali')

    # magic syntaxs
    '''
    pada page kali ini, penulis akan mencoba melihat apakah pelanggan akan pergi untuk selamanya atau tidak
    '''

    # show dataframe
    data = pd.read_csv('gabungandata.csv')
    st.dataframe(data)

    # membuat histogram berdasarkan input user
    st.write('#### Histogram berdasarkan Input user')
    pilihan = st.selectbox('pilih colomn: ', ('CreditScore', 'Age', 'Balance', 'EstimatedSalary', 'Balance'))
    fig = plt.figure(figsize= (15,5))
    sns.histplot(data[pilihan], bins=30, kde=True)
    st.pyplot(fig)

    # membuat plotly plot
    st.write('#### Plotly Plot - age with CreditScore')
    fig = px.scatter(data, x='Age', y= 'CreditScore', hover_data=['Exited'])
    st.plotly_chart(fig)

if __name__== '__main__':
    run()

