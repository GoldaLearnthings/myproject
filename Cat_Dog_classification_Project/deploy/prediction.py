from os import access
from PIL import Image
from io import BytesIO
import requests
import numpy as np
import streamlit as st
import tensorflow as tf

# Load Model
model = tf.keras.models.load_model('model_1.h5')

# Variable for image
img = None

# Prediction
def img_predict(img):
    pred = np.array(img)[:, :, :3]
    pred = tf.image.resize(pred, size=(220, 220))
    pred = pred / 255.0

    res = int(tf.round(model.predict(x=tf.expand_dims(pred, axis=0))))
    res = "YUP, THATS A CAT" if res == 0 else "YUP, THATS A DOG"
    title = f"<h2 style='text-align:center'>{res}</h2>"
    st.markdown(title, unsafe_allow_html=True)
    st.image(img, use_column_width=True)


def run():
    with st.form(key='pengecek gambar anjing atau kucing'):
        file = st.file_uploader("Upload", type=["jpg", "png", 'Tiff', 'jpeg', 'JPEG', 'JPG', 'PNG'])
        if file is not None:
            img = Image.open(file)

        submitted = st.form_submit_button('Predict')

    if submitted:
        if img is not None:
            img_predict(img)

if __name__== '__main__':
    run()