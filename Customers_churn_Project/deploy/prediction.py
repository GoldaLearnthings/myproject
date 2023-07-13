import streamlit as st
import pandas as pd
import numpy as np
import pickle 
import json

# Load All Files
with open('pipelines.pkl', 'rb') as file_1:
  clf_rfc = pickle.load(file_1)

with open('X_num_skew.txt', 'r') as file_2:
  X_num_skew = json.load(file_2)

with open('X_num_norm.txt', 'r') as file_3:
  X_num_norm = json.load(file_3)

with open('X_cat.txt', 'r') as file_4:
  X_cat = json.load(file_4)

def run():
    # membuat Tittle
    st.title('prediksi apakah konsumen anda pergi?')

    with st.form(key='form_prediksi_konsumen_minggat'):
        Surname = st.text_input('Surname', value='')
        Age = st.number_input('Age', min_value=18, max_value=80, step=1, help='Usia pelanggan?')
        Gender = st.radio('Gender', ('Male','Female'), index=1, help='jenis kelamin?')
        Geography = st.selectbox('Geography', ('Spain','France', 'Germany'), index=0, help='kebangsaan?')
        st.markdown('---')

        HasCrCard = st.selectbox('HasCrCard', (0,1), index=0, help='apakah anda kartu kredit?')
        IsActiveMember = st.selectbox('IsActiveMember', (0,1), index=0, help='apakah anda punya kartu member?')
        st.markdown('---')

        CreditScore = st.slider('CreditScore', 350, 850, 500)
        Tenure = st.slider('Tenure', 0, 10, 0)
        Balance = st.slider('Balance', 0, 250000, 50000)
        EstimatedSalary = st.slider('EstimatedSalary', 1000, 150000, 34000)
        NumOfProducts = st.slider('NumOfProducts', 1, 4, 1)
        
        submitted = st.form_submit_button('Predict')

    data_inf = {
        'Age': Age,
        'Gender': Gender,
        'Geography': Geography,
        'HasCrCard': HasCrCard,
        'IsActiveMember': IsActiveMember,
        'CreditScore': CreditScore,
        'Tenure': Tenure,
        'Balance': Balance,
        'EstimatedSalary': EstimatedSalary,
        'NumOfProducts': NumOfProducts,
    }

    data_inf = pd.DataFrame([data_inf])
    a = st.dataframe(data_inf)
    b = ('')

    if a == 0:
        b = 'tidak pergi'
    else:
        b = 'pergi'

    if submitted:

        y_pred_inf = clf_rfc.predict(data_inf)
        st.write('# apakah pelanggan anda pergi? \n', str(b))

if __name__== '__main__':
    run()

