import os
import streamlit as st
from PIL import Image
import openai

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
    st.markdown('<h1>Cuesta\'s AI Chatbot</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Verifica la ruta absoluta del archivo
context_file_path = "User Skills - Data Viz_Pipeline_Warehouse.xlsx"  # Ruta del archivo que contiene el contexto
st.write(f"Ruta absoluta: {os.path.abspath(context_file_path)}")

try:
    with open(context_file_path, "r", encoding="utf-8") as file:
        context = file.read()
except FileNotFoundError:
    st.error(f"Context file not found at: {context_file_path}")
    context = ""
except Exception as e:
    st.error(f"Error reading context file: {e}")
    context = ""

# Continúa con la lógica si el archivo se cargó correctamente
if not context:
    st.error("Error: Context file is empty or could not be loaded.")
else:
    # Preguntar al usuario por su OpenAI API Key
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.", icon="🗝️")
    else:
