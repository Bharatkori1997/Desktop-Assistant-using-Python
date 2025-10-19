import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os

#Taking voice from my system

speaker = pyttsx3.init("sapi5")

voices = speaker.getProperty('voices')
speaker.setProperty('voice',voices[1].id)

speaker.setProperty('rate',150)
speaker.setProperty('volume',0.8)

def text_to_voice(text):
    """This function takes text and return voice
    
    Args:
        text (_type_): string
    """
    speaker.say(text)
    speaker.runAndWait()

# speak('i will build my algo')

# Speech recognition function
def voice_to_text():
    """This funtion will recognise voice and return text

    Args:
        audio (_type_): sound
    """
    convert_audio = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        convert_audio.pause_threshold=1
        b_audio = convert_audio.listen(source)

        try:
            print('Recognising....')
            b_to_text = convert_audio.recognize_google(b_audio)
            print(f'you said: {b_to_text}')

        except Exception as e:
            print('Say that again as please')
            return None
        return b_to_text
    
text = voice_to_text()

text_to_voice(text)
# print(sr.__version__)

