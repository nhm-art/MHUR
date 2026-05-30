import streamlit as st
import os
from google.genai import client
from google.genai import types
from gtts import gTTS

st.title("M'hur")
st.write("Welcome to your AI Tutor!")

api_key = st.secrets["api_key"]
client = genai.Client(api_key=api_key)

uploaded_file = st.file_uploader("Choose a PDF or PowerPoint file")

if uploaded_file is not None:
    st.write("Generating explanation...")
    file_bytes = uploaded_file.read()
    
    file_part = types.Part.from_bytes(
        data=file_bytes,
        mime_type=uploaded_file.type,
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            file_part,
            "Provide a tutorial explanation of this file as a study guide."
        ]
    )
    
    explanation = response.text
    st.write(explanation)
    
    st.write("Generating audio...")
    tts = gTTS(text=explanation, lang='en')
    tts.save("explanation.mp3")
    
    st.audio("explanation.mp3")
