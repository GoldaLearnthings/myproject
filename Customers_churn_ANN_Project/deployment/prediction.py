import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import pickle 
import json


# Load All Files
with open('final_pipeline.pkl', 'rb') as file_1:
  final_pipeline = pickle.load(file_1)

with open('num_skew.txt', 'r') as file_2:
  num_skew = json.load(file_2)

with open('num_norm.txt', 'r') as file_3:
  num_norm = json.load(file_3)

with open('cat_columns.txt', 'r') as file_4:
  cat_columns = json.load(file_4)

model_ann = load_model('churn.h5')

def run():
  with st.form(key='form_prediksi_konsumen_minggat'):
      age = st.number_input('age', min_value=18, max_value=80, step=1, help='Usia pelanggan?')
      gender = st.radio('gender', ('F','M'), index=1, help='jenis kelamin?')
      region_category = st.selectbox('region_category', ('City','Village', 'Town'), index=0, help='tempat konsumen?')
      membership_category = st.selectbox('membership_category', ('Basic Membership','Gold Membership', 'No Membership','Platinum Membership', 'Premium Membership', 'Silver Membership'), index=0, help='jenis member konsumen?')
      joined_through_referral = st.selectbox('joined_through_referral', ('No','Yes'), index=0, help='Masuk dengan referensi?')
      preferred_offer_types = st.selectbox('preferred_offer_types', ('Credit/Debit Card Offers','Gift Vouchers/Coupons', 'Without Offers'), index=0, help='type of offer?')
      medium_of_operation = st.selectbox('medium_of_operation', ('Both','Desktop', 'Smartphone'), index=0, help='mengakses toko dengan?')
      used_special_discount = st.selectbox('used_special_discount', ('No','Yes'), index=0, help='Belanja dengan diskon?')
      offer_application_preference = st.selectbox('offer_application_preference', ('Yes','No'), index=0, help='memberi tahu bila ada penawaran khusus?')
      past_complaint = st.selectbox('past_complaint', ('Yes','No'), index=0, help='pernah komplain?')
      internet_option = st.selectbox('internet_option', ('Wi-Fi','Mobile_Data', 'Fiber_Optic'), index=0, help='online menggunakan?')
      complaint_status = st.selectbox('complaint_status', ('Not Applicable','Unsolved', 'Solved', 'Solved in Follow-up', 'No Information Available'), index=0, help='status komplain?')
      feedback = st.selectbox('feedback', ('No reason specified','Poor Customer Service', 'Poor Product Quality', 'Poor Website', 'Products always in Stock', 'Quality Customer Care', 'Reasonable Price', 'Too many ads', 'User Friendly Website'), index=0, help='type of feedback?')

      days_since_last_login = st.slider('days_since_last_login', -999, 26, 0)
      avg_time_spent = st.slider('avg_time_spent', 0, 3000, 0)
      avg_transaction_value = st.slider('avg_transaction_value', 900, 850000, 50000)
      avg_frequency_login_days = st.slider('avg_frequency_login_days', 0, 73, 5)
      points_in_wallet = st.slider('points_in_wallet', 0, 2000, 1)
      
      submitted = st.form_submit_button('Predict')


  data_inf = {
      'age': age,
      'gender': gender,
      'region_category': region_category,
      'membership_category': membership_category,
      'joined_through_referral': joined_through_referral,
      'preferred_offer_types': preferred_offer_types,
      'medium_of_operation': medium_of_operation,
      'used_special_discount': used_special_discount,
      'offer_application_preference': offer_application_preference,
      'past_complaint': past_complaint,
      'complaint_status': complaint_status,
      'feedback': feedback,
      'days_since_last_login': days_since_last_login,
      'avg_time_spent': avg_time_spent,
      'avg_transaction_value': avg_transaction_value,
      'avg_frequency_login_days': avg_frequency_login_days,
      'points_in_wallet': points_in_wallet,
      'internet_option': internet_option
  }

  data_inf = pd.DataFrame([data_inf])
  data_inf

  if submitted:
      y_pred_inf = final_pipeline.transform(data_inf)
      
      y_pred_inf = model_ann.predict(y_pred_inf)
      y_pred_inf = np.where(y_pred_inf >= 0.5, 'ya', 'tidak')

      st.write('# apakah pelanggan anda pergi? \n', y_pred_inf)

if __name__== '__main__':
    run()