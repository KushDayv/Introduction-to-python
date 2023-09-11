import os
import time
import pyaudio
import speech_recognition as sr
import playsound
from gtts import gTTS
import openai
import uuid

api_key = "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"
lang = 'en'

openai.api_key = api_key

guy = ""

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
            global guy
            guy = said

            if "Jarvis" in said:
                new_string = said.replace("Jarvis", "")
                new_string = new_string.strip()
                print(new_string)
                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": new_string}])
                text = completion.choices[0].message.content
                speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                file_name = f"welcome_{str(uuid.uuid4())}.mp3"
                speech.save(file_name)
                playsound.playsound(file_name, block=False)

        except Exception as e:
            print(f"Exception: {str(e)}")

    return said

while True:
    if "stop" in guy:
        break

    get_audio()