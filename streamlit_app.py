import streamlit as st
from openai import OpenAI

# CSS para fijar el logo en la parte superior derecha
st.markdown(
    """
    <style>
    .image-container {
        position: fixed;
        top: 5px;
        right: 20px;
        z-index: 1;
    }
    .image-container img {
        width: 150px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Coloca el logo en la parte superior
with st.container():
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image("cuesta-logo.png", use_column_width=False)
    st.markdown('</div>', unsafe_allow_html=True)

# Show title and description.
st.title("Cuesta's AI Chatbot")
st.write(
    "This is a Cuesta chatbot that uses OpenAI's GPT-3.5 model to generate responses based on internal data."
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("Ask me anything related to the Cuesta's internal data?"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
