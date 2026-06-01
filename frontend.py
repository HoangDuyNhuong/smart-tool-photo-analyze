import streamlit as st
from backend import ask_model_on_image

st.set_page_config(page_title="Vision AI", layout="centered")

st.title("🧠 Vision AI")
st.write("Pose une question sur une image")

uploaded_file = st.file_uploader("📷 Upload image", type=["jpg", "jpeg", "png"])
question = st.text_input("❓ Question")

if uploaded_file:
    st.image(uploaded_file, caption="Image", use_container_width=True)

    if st.button("Analyser"):
        if not question.strip():
            st.warning("Entre une question")
        else:
            with st.spinner("Analyse..."):
                try:
                    image_bytes = uploaded_file.read()
                    response = ask_model_on_image(question, image_bytes)

                    st.success("Réponse")
                    st.write(response)

                except Exception as e:
                    st.error(str(e))