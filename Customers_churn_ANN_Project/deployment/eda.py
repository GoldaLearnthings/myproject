import streamlit as st
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
   page_title= 'Churn Consumers',
   layout='wide',
   initial_sidebar_state='expanded'
)

# membuat Tittle
st.title('Churn Prediction')

# magic syntax
'''
Prediksi *churn* adalah proses memprediksi kemungkinan pelanggan atau pengguna berhenti menggunakan produk atau layanan suatu perusahaan. 
'''
'''
Memprediksi churn penting karena dapat membantu perusahaan memahami perilaku pelanggan atau pengguna, mengidentifikasi masalah yang mungkin menyebabkan pelanggan atau pengguna berhenti menggunakan produk atau layanan, dan membuat strategi yang lebih efektif dalam mempertahankan pelanggan atau pengguna. Dengan memprediksi churn, perusahaan dapat mengurangi biaya akuisisi pelanggan baru dan meningkatkan pendapatan dengan mempertahankan pelanggan atau pengguna yang sudah ada.
'''
st.markdown('---')

# show dataframe
data = pd.read_csv('churn.csv')
st.dataframe(data)

image = Image.open('description.png')
st.image(image, caption='dataset description')

st.markdown('---')

# membuat barplot
st.write('#### plot untuk churn_risk_score')
fig = plt.figure(figsize= (15,5))
sns.countplot(x= 'churn_risk_score', data=data)
st.pyplot(fig)

st.write('#### plot untuk gender berdasarkan churn_risk_score')
fig = plt.figure(figsize= (15,5))
sns.countplot(x='gender' ,hue= 'churn_risk_score', data=data)
st.pyplot(fig)

st.write('#### plot untuk region_category berdasarkan churn_risk_score')
fig = plt.figure(figsize= (15,5))
sns.countplot(x='region_category' ,hue= 'churn_risk_score', data=data)
st.pyplot(fig)

st.write('#### plot untuk membership_category berdasarkan churn_risk_score')
fig = plt.figure(figsize= (15,5))
sns.countplot(x='membership_category' ,hue= 'churn_risk_score', data=data)
st.pyplot(fig)

st.write('#### plot untuk preferred_offer_types berdasarkan churn_risk_score')
fig = plt.figure(figsize= (15,5))
sns.countplot(x='preferred_offer_types' ,hue= 'churn_risk_score', data=data)
st.pyplot(fig)

st.write('#### plot untuk feedback berdasarkan churn_risk_score')
fig = plt.figure(figsize= (15,5))
sns.countplot(x='feedback' ,hue= 'churn_risk_score', data=data)
st.pyplot(fig)
st.markdown('---')

# Membuat Histogram Berdasarkan Input User
st.write('#### Histogram Based On User Input')
pilihan = st.selectbox('Choose Column : ', ('age', 'days_since_last_login', 'avg_time_spent', 
                                          'avg_transaction_value', 'avg_frequency_login_days', 'points_in_wallet'))
fig = plt.figure(figsize=(15,5))
sns.histplot(data[pilihan], bins=30, kde=True)
st.pyplot(fig)

st.markdown('---')
'''webpage kali ini digunakan dalam program pembelajaran di hactiv8'''