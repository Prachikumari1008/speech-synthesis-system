# speech-synthesis-system

Open your terminal and run the following command to start the Streamlit app: streamlit run app.py 

This will start the Streamlit server and open a new tab in your default web browser showing the app.


## Explanation of the Code

Imports: Import the necessary modules.

translate_and_speak function: This function uses deep-translator to translate the text from English to the selected Indian language and gTTS to convert the translated text to speech, saving it as an MP3 file.

Page Configuration: Set the page configuration for the Streamlit app.

Custom CSS: Add custom CSS to style the app with a dark theme and a green button. The button's background color is set to green, and it changes to a darker green when hovered over.

## Streamlit UI:
- The title and description of the app.
- A text area for users to input the text they want to translate from English and convert to speech.
- A dropdown to select the destination language for the translation and text-to-speech conversion, focusing on Indian languages.
- A button that triggers the translation and conversion.
- An audio player to play the generated MP3 file.
- Instructions for using the app.
- 
This script provides a dark-themed UI  for translating text from English to different Indian languages and converting the translated text to speech in your Streamlit application.
