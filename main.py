import speech_recognition as sr
from time import ctime
import os
import playsound
from gtts import gTTS
import requests

r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print("Sorry, my speech service is down")
        return voice_data

def respond(voice_data):
    if "what is your name" in voice_data:
        speak("My name is Jarvis")

    if "what time is it" in voice_data:
        speak(ctime())

    if "what is my location" in voice_data:
        res = requests.get("https://ipinfo.io/")
        data = res.json()
        city = data["city"]
        timezone = data["timezone"]
        speak("You are in" + city + "And" + "Your Timezone is" + timezone)

    if "how are you" in voice_data:
        speak("im well and you and I hope you are too")

    if "what sport do you like" in voice_data:
        speak("I like Tennis and Formula 1")

    if "save a name" in voice_data:
        newName = input("Type a name: ")

        name = open("names.txt", "r")
        names = name.read()
        print(names)

        name_file = open("names.txt", "w")
        name_file.write(names + "\n" + newName + "\n")
        name_file.close()

    if "clear all names" in voice_data:
        name_file = open("names.txt", "w")
        name_file.write("")
        name_file.close()

        speak("Cleared all names!")

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "answer.mp3"
    tts.save(filename)
    playsound.playsound(filename)

print("Hello, how can i help you?")
voice_data = record_audio()
respond(voice_data)