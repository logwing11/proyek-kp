import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import tempfile


# Fungsi untuk memuat model
def load_selected_model(model_path):
    return load_model(model_path)


# Fungsi untuk memprediksi gambar
def predict_image(model, img):
    img = img.resize((224, 224))  # Sesuaikan dengan input model Anda
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    return predictions


# Fungsi untuk mengubah prediksi menjadi label
def map_prediction_to_label(prediction, threshold=0.5):
    if prediction >= threshold:
        return "dusty"
    else:
        return "clean"


def show_user():
    # Main Streamlit app
    st.title("Deteksi Debu pada Panel Surya")
    st.write(
        "Aplikasi ini memungkinkan Anda untuk mendeteksi apakah panel surya bersih atau berdebu."
    )

    option = st.selectbox("Pilih Model", ("Model Bawaan", "Upload Model Sendiri"))

    model = None
    if option == "Model Bawaan":
        model_path = "mode/solar_panel_model_MNV.h5"
        try:
            model = load_selected_model(model_path)
            st.success("Model Bawaan Berhasil Dimuat!")
        except OSError as e:
            st.error(f"Kesalahan: {e}")
    elif option == "Upload Model Sendiri":
        uploaded_model = st.file_uploader("Unggah file model .h5", type=["h5"])
        if uploaded_model is not None:
            try:
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(uploaded_model.read())
                    temp_model_path = temp_file.name
                model = load_model(temp_model_path)
                st.success("Model Anda Berhasil Dimuat!")
            except Exception as e:
                st.error(f"Kesalahan: {e}")

    uploaded_image = st.file_uploader(
        "Unggah gambar untuk diprediksi", type=["jpg", "png", "jpeg"]
    )

    if uploaded_image is not None and model is not None:
        img = Image.open(uploaded_image)
        st.image(img, caption="Gambar yang diunggah", use_column_width=True)
        predictions = predict_image(model, img)
        label = map_prediction_to_label(
            predictions[0][0]
        )  # Ambil prediksi pertama dari array
        st.write(f"Hasil Prediksi: {label}")
