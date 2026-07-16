import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="📖 AI Story Generator", page_Icon="📕")
st.title("📖 AI Story Generator")
st. write("Generate creative stories using GPT-2")


# Load GPT-2 only once
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

topic = st.text_input(
    "Story Topic",
    placeholder="A dragon that loves pizza"
)

genre = st.selectbox(
    "Genre",
    [
        "Adventure",
        "Fantasy",
        "Sci-Fi",
        "Mystery",
        "Comedy",
        "Horror"
    ]
)

length = st.slider(
    "Story Length",
    100,
    400,
    200,
    step=50
)

if st.button("✨ Generate Story"):

    if topic.strip() == "":
        st.warning("Please enter a story topic.")
        st.stop()

    prompt = f"""
Title: {topic}

Genre: {genre}

Story:

Once upon a time,
"""
    
    with st.spinner("AI is writing your story..."):

        result = generator(
            prompt,
            max_new_tokens=length,
            temperature=0.9,
            do_sample=True,
            top_p=0.95,
            repetition_penalty=1.2,
            pad_token_id=50256
        )

    story = result[0]["generated_text"]

    # Remove the prompt
    story = story.replace(prompt, "").strip()

    st.subheader("📕 Your Story")
    st.write(story)