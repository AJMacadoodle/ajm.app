import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Language Translator", page_icon="🌎")

st.title("🌎 AI Language Translator")
st.write("Translate English into different languages.")

@st.cache_resource
def load_model():
    return pipeline(
        "translation",
        model="Helsinki-NLP/opus-mt-en-fr"
    )

translator = load_model()

languages = {
    "French":"Helsinki-NLP/opus-mt-en-fr",
    "German":"Helsink1-NLP/opus-mt-en-de"
    "Spanish":"Helsink1-NLP/opus-mt-en-es"
    "Italian":"HelsinkI-NLP/opus-mt-en-it"
}

language = st.selectbox(
    "Select Language",
    list(languages.keys())
)

text = st.text_area("Enter English Text")

if st.button("Translate"):

    with st.spinner("Loading model..."):

        translator = pipeline(
            "translation",
            model=languages[language]
        )

        result = translator(text)

        st.success(result[0]["translation_text"])