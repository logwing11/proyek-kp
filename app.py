import streamlit as st
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth
import a
import b
import json

# Konfigurasi Pyrebase
firebase_config = {
    "apiKey": "AIzaSyAyDi7f4MidQYAUIv7ymKI6hq6xfFp4Las",
    "authDomain": "solar-panel-73244.firebaseapp.com",
    "databaseURL": "https://solar-panel-73244-default-rtdb.firebaseio.com",
    "projectId": "solar-panel-73244",
    "storageBucket": "solar-panel-73244.appspot.com",
    "messagingSenderId": "585463005418",
    "appId": "1:585463005418:web:adfab22c4f5c4585519793",
    "measurementId": "G-XFPJBVS1FE",
}


# Inisialisasi Pyrebase
firebase = pyrebase.initialize_app(firebase_config)
auth_pyrebase = firebase.auth()

# Inisialisasi Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate("solar-panel.json")
    firebase_admin.initialize_app(cred)


# Fungsi untuk menambahkan klaim admin ke pengguna
def add_admin_claim(email):
    try:
        user = auth.get_user_by_email(email)
        auth.set_custom_user_claims(user.uid, {"admin": True})
        print(f"Admin claim added to user {email}")
    except Exception as e:
        print(f"Error adding admin claim: {e}")


# Fungsi untuk mendapatkan klaim pengguna
def get_user_claims(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token.get("admin", False)
    except Exception as e:
        print(f"Error getting user claims: {e}")


st.title("Solar Panel Dust Detection")

# Initialize session state for sign up and login
if "signup" not in st.session_state:
    st.session_state.signup = False
if "login" not in st.session_state:
    st.session_state.login = False
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
if "token" not in st.session_state:
    st.session_state.token = None

# Render halaman berdasarkan status login
if st.session_state.is_logged_in:
    if st.session_state.is_admin:
        st.success("Welcome Admin!")
        a.show_appadmin()  # Panggil fungsi dari app.py
    else:
        st.success("Welcome User!")
        b.show_appuser()  # Panggil fungsi dari user.py

    if st.sidebar.button("Logout", key="logout"):
        st.session_state.is_logged_in = False
        st.session_state.is_admin = False
        st.session_state.token = None
        st.experimental_rerun()
else:
    # Sign Up
    if st.button("Sign Up", key="go_to_signup"):
        st.session_state.signup = True
        st.session_state.login = False

    if st.session_state.signup:
        st.subheader("Sign Up")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_password")

        if st.button("Submit Sign Up", key="submit_signup"):
            if email and password:
                try:
                    user = auth_pyrebase.create_user_with_email_and_password(
                        email, password
                    )
                    st.success("User registered successfully!")
                    # Menambahkan klaim admin jika email adalah admin
                    if email == "awingmn12@gmail.com":
                        add_admin_claim(email)
                except Exception as e:
                    if "EMAIL_EXISTS" in str(e):
                        st.error("Email sudah terdaftar. Silakan gunakan email lain.")
                    elif "WEAK_PASSWORD" in str(e):
                        st.error(
                            "Kata sandi terlalu lemah. Gunakan setidaknya 6 karakter."
                        )
                    else:
                        st.error("Terjadi kesalahan saat pendaftaran.")

    # Login
    if st.button("Log In", key="go_to_login"):
        st.session_state.login = True
        st.session_state.signup = False

    if st.session_state.login:
        st.subheader("Log In")
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Submit Log In", key="submit_login"):
            if email and password:
                try:
                    user = auth_pyrebase.sign_in_with_email_and_password(
                        email, password
                    )
                    token = user["idToken"]
                    st.session_state.is_logged_in = True
                    st.session_state.token = token
                    st.session_state.is_admin = get_user_claims(token)
                    st.success("Logged in successfully!")
                    st.experimental_rerun()  # Refresh halaman setelah login
                except Exception as e:
                    if "INVALID_PASSWORD" in str(e):
                        st.error("Kata sandi salah. Silakan coba lagi.")
                    elif "EMAIL_NOT_FOUND" in str(e):
                        st.error(
                            "Email tidak ditemukan. Silakan periksa kembali email Anda."
                        )
                    else:
                        st.error("Terjadi kesalahan saat login.")

    if not st.session_state.signup and not st.session_state.login:
        st.info("Please log in or sign up to access the application.")
