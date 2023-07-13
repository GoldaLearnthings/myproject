import streamlit as st
import pandas as pd
import numpy as np
import pickle 
import json

# Load All Files
with open('Adaboost.pkl', 'rb') as file_1:
  Ada_best = pickle.load(file_1)

with open('randomForest.pkl', 'rb') as file_2:
  rnd_best = pickle.load(file_2)

with open('model_scaler.pkl', 'rb') as file_3:
  model_scaler = pickle.load(file_3)

with open('model_encoder.pkl','rb') as file_4:
  model_encoder = pickle.load(file_4)

with open('list_num_cols.txt', 'r') as file_5:
  list_num_cols = json.load(file_5)

with open('list_cat_cols.txt', 'r') as file_6:
  list_cat_cols = json.load(file_6)

def run():
    # membuat Tittle
    st.title('prediksi berapa banyak jantung yang telah anda gagalkan')

    with st.form(key='form_prediksi_gagal_jantung'):
        age = st.number_input('Age', min_value=40, max_value=90, step=1, help='Usia Pasien')
        sex = st.selectbox('sex', (0,1), index=0, help='apakah anda punya penis?')
        st.markdown('---')

        anaemia = st.selectbox('anaemia', (0,1), index=0, help='apakah anda punya anemia?')
        diabetes = st.selectbox('diabetes', (0,1), index=0, help='apakah anda punya diabetes?')
        high_blood_pressure = st.selectbox('high_blood_pressure', (0,1), index=0, help='apakah anda punya darah tinggi?')
        smoking = st.selectbox('smoking', (0,1), index=0, help='apakah anda merokok?')
        st.markdown('---')

        platelets = st.slider('platelets', 30000, 800000, 30000)
        creatinine_phosphokinase = st.slider('creatinine_phosphokinase', 25, 7500, 50)
        ejection_fraction = st.slider('ejection_fraction', 15, 75, 20)
        serum_creatinine = st.slider('serum_creatinine', 0.5, 9.0, 1.0)
        serum_sodium = st.slider('serum_sodium', 115, 140, 120)
        time = st.slider('time', 5, 280, 30)
        
        submitted = st.form_submit_button('Predict')

    data_inf = {
        'age': age,
        'sex': sex,
        'anaemia': anaemia,
        'diabetes': diabetes,
        'high_blood_pressure': high_blood_pressure,
        'smoking': smoking,
        'platelets': platelets,
        'creatinine_phosphokinase': creatinine_phosphokinase,
        'ejection_fraction': ejection_fraction,
        'serum_creatinine': serum_creatinine,
        'serum_sodium': serum_sodium,
        'time': time
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:

        # Split between Numerical Columns and Categorical Columns

        data_inf_num = data_inf[list_num_cols]
        data_inf_cat = data_inf[list_cat_cols]

        # Feature Scaling and Feature Encoding

        data_inf_num_scaled = model_scaler.transform(data_inf_num)
        data_inf_cat_encoded = model_encoder.transform(data_inf_cat)
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis=1)

        # Predict using Adaboost

        y_pred_inf = Ada_best.predict(data_inf_final)
        st.write('# berapa banyak jantung yang akan anda gagalkan? ', str(int(y_pred_inf)))

if __name__== '__main__':
    run()
