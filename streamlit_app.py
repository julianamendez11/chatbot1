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

# Descripción debajo del título y logo
st.write(
    "This is a Cuesta chatbot that uses OpenAI's GPT-3.5 model to generate responses based on internal data."
)

# Carga el archivo de contexto al inicio (por ejemplo, un archivo .txt que contiene la información base)
context_file_path = "User Skills - Data Viz_Pipeline_Warehouse.xlsx"  # Ruta del archivo que contiene el contexto
try:
    with open(context_file_path, "r", encoding="utf-8") as file:
        context = file.read()
except FileNotFoundError:
    st.error(f"Context file not found: {context_file_path}")
    context = ""

# Preguntar al usuario por su OpenAI API Key
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:
    # Crear cliente OpenAI
    openai.api_key = openai_api_key

    # Crear una variable de estado para almacenar los mensajes
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar los mensajes del chat existentes
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Campo de entrada para que el usuario haga preguntas
    if prompt := st.chat_input("Ask me anything related to the Cuesta's internal data?"):
        # Guardar y mostrar el prompt del usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generar una respuesta usando la API de OpenAI, basándose en el contexto
        # El contexto se pasa como el mensaje inicial para guiar las respuestas del modelo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are an assistant. Use only the following context to answer the user: {context}"},
                {"role": "user", "content": prompt}
            ]
        )

        # Mostrar la respuesta en el chat y guardarla en el estado de la sesión
        assistant_response = response['choices'][0]['message']['content']
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
