import streamlit as st

# Fungsi untuk menampilkan halaman-halaman aplikasi
from mode.user import show_user
from mode.bantu import help


def show_appuser():
    # Menambahkan judul dan logo di bagian atas aplikasi
    st.image("40.jpeg", width=200)
    st.sidebar.title("PILIH MENU")

    # Tambahkan menu-menu ke sidebar
    menu_selection = st.sidebar.radio(
        "",
        [
            "Deteksi Debu",
            "Bantuan",
        ],
    )

    # Logika untuk menavigasi ke halaman yang dipilih
    if menu_selection == "Deteksi Debu":
        show_user()
    elif menu_selection == "Bantuan":
        help()
