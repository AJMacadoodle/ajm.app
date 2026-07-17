import streamlit as st
from transformers import pipeline

# Configure the page settings
st.set_page_config(page_title="🚗 AI Traffic Advisor", page_Icon="🚦")
st.title("🚗 AI Traffic Advisor")
st.write("Get effective driving advice using GPT-2")

# Cache the model pipeline so it only loads once
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt-2")

generator = load_model()

# User interface inputs
user_query = st.text_input(
    "Describe your traffic situation or ask a question:",
    placeholder="e.g., I am stuck in heavy rain on the highway. What should I do?"
)

max_length = st.slider("Response length (tokens):", min_value=20, max_value=150, value=60)

# Generate and display advice
if st.button("Get AI Advice"):
    if user_query:
        with st.spinner("Analyzing traffic situation..."):
            # Clean text generation settings
            results = generator(
                user_query, 
                max_length=max_length, 
                num_return_sequences=1,
                truncation=True
            )
            advice = results[0]["generated_text"]
            
            st.subheader("🚦 Smart Advisor Suggestion:")
            st.write(advice)
    else:
        st.warning("Please enter a traffic scenario first.")