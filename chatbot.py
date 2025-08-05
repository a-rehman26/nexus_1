import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

client = genai.Client(api_key=api_key)

st.title("AI Explanation Generator")

user_input = st.text_input("Enter a prompt:", "Explain how AI works in a few words")

if st.button("Generate Explanation"):
    if user_input.strip():
        with st.spinner("Generating..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input,
            )
        st.subheader("AI Explanation:")
        st.write(response.text)
    else:
        st.error("Please enter a prompt to generate content.")
 