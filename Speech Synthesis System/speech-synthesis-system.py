import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator

# Function to translate text and convert it to speech
def translate_and_speak(text,dest_lang):
    translated_text = GoogleTranslator(source='en', target=dest_lang).translate(text)
    tts = gTTS(text=translated_text, lang=dest_lang)
    tts.save("output.mp3")
    return translated_text

# Set page configuration
st.set_page_config(
    page_title="Text to Speech and Translator",
    page_icon="🎤",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for dark theme styling with good font color contrast
st.markdown("""
    <style>
    body {
        background-color: #0E1117;
        color: #CFCFCF;
    }
    .main {
        background-color: #161B22;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .title {
        font-size: 2.5rem;
        color: #79DAE8;
        text-align: center;
        font-weight: bold;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #B0BEC5;
        text-align: center;
        margin-bottom: 20px;
    }
    .stTextArea, .stSelectbox, .stButton {
        background-color: #1E2229;
        color: #CFCFCF;
        border-radius: 10px;
    }
    .stTextArea textarea {
        background-color: #1E2229;
        color: #CFCFCF;
    }
    .stSelectbox div {
        background-color: #1E2229;
        color: #CFCFCF;
    }
    .convert-button {
        background-color: #04AA6D; /* Green */
        border: none;
        color: white;
        font-size: 1rem;
        padding: 10px 20px;
        border-radius: 10px;
        margin-top: 20px;
        cursor: pointer;
    }
    .convert-button:hover {
        background-color: #56A8C3;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
#st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">Text to Speech and Translator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter text below to translate from English to an Indian language and convert to speech</div>', unsafe_allow_html=True)

# Text input
text_input = st.text_area("Text to translate and convert to speech:", height=30, key="textarea", help="Enter the text you want to translate and convert to speech", placeholder="Type your text here...")

# Source language selection
indian_languages = {
    'English': 'en',
    'Hindi': 'hi',
    'Bengali': 'bn',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Marathi': 'mr',
    'Gujarati': 'gu',
    'Kannada': 'kn',
    'Malayalam': 'ml',
    'Urdu': 'ur'
}

# Destination language selection
dest_language = st.selectbox("Select Destination Language", list(indian_languages.keys()), help="Select the destination language for text-to-speech conversion")

# Translate and Convert button
if st.button("Translate and Convert", key="convert_button", use_container_width=True):
    if text_input:
        translated_text = translate_and_speak(text_input,dest_lang=indian_languages[dest_language])
        st.markdown(f"**Translated Text:** {translated_text}")
        st.audio("output.mp3", format="audio/mp3")
    else:
        st.warning("Please enter some text to translate and convert to speech", icon="⚠️")

st.markdown('</div>', unsafe_allow_html=True)

# Instructions
st.write("""
    This app uses Google Translate and Google Text-to-Speech to translate text and convert it to speech. 
    Enter text above, select the source and destination languages, and click the translate and convert button to generate the audio.
""")
