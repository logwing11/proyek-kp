import streamlit as st

# Fungsi untuk menampilkan halaman-halaman aplikasi
from mode.mnv import show_mnv
from mode.dn import show_dn
from mode.iv import show_iv
from mode.x import show_x
from mode.pilih import show_choose
from mode.bantu import help


def show_appadmin():
    # Menambahkan judul dan logo di bagian atas aplikasi
    st.image("40.jpeg", width=200)
    st.sidebar.title("PILIH MODEL")

    # Tambahkan menu-menu ke sidebar
    menu_selection = st.sidebar.radio(
        "",
        [
            "MobileNetV2",
            "DenseNet121",
            "InceptionV3",
            "Xception",
            "Coba Model Lainnya",
            "Bantuan",
        ],
    )

    # Logika untuk menavigasi ke halaman yang dipilih
    if menu_selection == "MobileNetV2":
        show_mnv()
    elif menu_selection == "DenseNet121":
        show_dn()
    elif menu_selection == "InceptionV3":
        show_iv()
    elif menu_selection == "Xception":
        show_x()
    elif menu_selection == "Coba Model Lainnya":
        show_choose()
    elif menu_selection == "Bantuan":
        help()
