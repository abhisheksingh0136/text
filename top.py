import streamlit as st
import google.generativeai as genai
import os

# Configuration
os.environ["GOOGLE_API_KEY"] = "AIzaSyCjIzxSgv48nm6Ww36beoX5Xel3NqKUIsw"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Initialize model
generation_config = {"temperature": 0.9, "top_p": 1, "top_k": 1, "max_output_tokens": 2048}
model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)

# Streamlit UI
st.title("Text Generation Content")
st.title("🤖Summarizer🤖")

# Input text area
input_text = st.text_area("Enter the text:", height=400)

# Selection for action
action = st.radio("Choose Action:", ("Generate Summary", "Generate Topic","Generate Key Points"))

# Perform action based on selection
if action == "Generate Summary":
    if st.button("Generate Summary"):
        # Generate summary
        summary_prompt = "Generate the summary of the text."
        response = model.generate_content([summary_prompt, input_text])
        summary_text = response.text
        st.subheader("Generated Summary:")
        st.text_area("Summary", value=summary_text, height=300)

# Perform action based on selection
elif action == "Generate Key Points":
    if st.button("Generate Key Points"):
        # Generate summary
        summary_prompt = """Generate key points summarizing the details."""
        response = model.generate_content([summary_prompt, input_text])
        summary_text = response.text
        st.subheader("Generated Key Points:")
        st.text_area("Key Points", value=summary_text, height=300)

elif action == "Generate Topic":
    if st.button("Generate Topic"):
        # Generate summary
        summary_prompt = "Generate the summary of the text."
        response = model.generate_content([summary_prompt, input_text])
        summary_text = response.text

        # Generate topic
        topic_prompt = "Ggenerate the topic of the summary"
        response = model.generate_content([topic_prompt, summary_text])
        topic_text = response.text
        st.subheader("Generated Topic:")
        st.text_area("Topic", value=topic_text, height=100)
