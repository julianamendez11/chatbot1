import streamlit as st
from PIL import Image

# CSS para colocar la imagen encima del título, sin espacio entre ellos
st.markdown(
    """
    <style>
    .header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 0px;
    }
    .header-container img {
        width: 150px;
        margin-bottom: 0px;
    }
    h1 {
        margin-top: 0;
        margin-bottom: 0;
        padding-bottom: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Carga la imagen del logo
try:
    logo = Image.open("cuesta-logo.png")  # Actualiza el path si es necesario
except FileNotFoundError:
    st.error("Image file not found. Please check the file path.")

# Coloca el logo encima del título
with st.container():
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    if logo:
        st.image(logo, use_column_width=False)
    st.markdown('<h1>💬 Cuesta\'s Data Team Skills AI Chatbot</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Descripción debajo del título y logo
st.write(
    "This is a Cuesta chatbot that uses OpenAI's GPT-3.5 model to generate responses based on internal data."
)
