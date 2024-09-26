import streamlit as st
from openai import OpenAI

# CSS para posicionar el logo junto al título, sin espacio adicional
st.markdown(
    """
    <style>
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0px;
    }
    .header-container img {
        width: 150px;
        margin-right: 10px;
    }
    h1 {
        margin-top: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Coloca el logo junto al título
with st.container():
    st.markdown(
        """
        <div class="header-container">
            <img src="cuesta-logo.png" alt="Cuesta Logo">
            <h1>💬 Cuesta's Data Team Skills AI Chatbot</h1>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Descripción debajo del título y logo
st.write(
    "This is a Cuesta chatbot that uses OpenAI's GPT-3.5 model to generate responses based on internal data."
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key
