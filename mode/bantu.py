import streamlit as st


import streamlit as st


def help():
    st.markdown(
        """
        <style>
        .help-container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background-color: #f4f4f4;
            border-radius: 10px;
        }
        .contact-info {
            margin-top: 20px;
        }
        </style>
        <div class="help-container">
            <h2>Pusat Bantuan</h2>
            <div class="contact-info">
                <h3>Nomor Telepon/Whatsapp</h3>
                <p>088888888888</p>
                <h3>Email</h3>
                <p>kamiber5@gmail.com</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
