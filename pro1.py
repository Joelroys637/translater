import streamlit as st
from googletrans import Translator
from gtts import gTTS
from io import BytesIO

def translate_text(text, src_lang='en', dest_lang='ta'):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def text_to_speech(text, lang='ta'):
    tts = gTTS(text=text, lang=lang)
    fp = BytesIO()
    tts.write_to_fp(fp)
    return fp.getvalue()

def main():
    st.title("English to Tamil Translator")

    # Input text box for English text
    input_text = st.text_area("Enter English text:", height=200)

    # Translate button
    if st.button("Translate"):
        translated_text = translate_text(input_text)
        st.write("Translated Tamil text:")
        st.write(translated_text)

        # Text-to-speech button
        if st.button("Listen to Translation"):
            audio_data = text_to_speech(translated_text,lang='ta')
            st.audio(audio_data, format='audio/mp3')

if __name__ == "__main__":
    main()
