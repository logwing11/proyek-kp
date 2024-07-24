import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Memuat model yang telah dilatih
model_dn = tf.keras.models.load_model("mode/solar_panel_model_DN.h5")


# Fungsi untuk prediksi gambar
def predict_image_dn(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model_dn.predict(img_array)
    return "Dusty" if prediction[0] > 0.5 else "Clean"


# Streamlit interface
def show_dn():
    st.title("DENSENET121")
    st.write("Upload an image of a solar panel to check if it is dusty or clean.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        st.write("Hasil Prediksi...")
        label = predict_image_dn(img)
        st.write(f"Hasil Prediksi: {label}")
