import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyjokes
import os
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        return command

def volume_up():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(1.0, None)

def volume_down():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(0.2, None)

def run_assistant():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'open google' in command:
        talk("Opening google")
        os.system("start chrome")

    elif 'open notepad' in command:
        talk("Opening notepad")
        os.system("notepad")

    elif 'shutdown' in command:
        talk("Shutting down system")
        os.system("shutdown /s /t 1")

    elif 'volume up' in command:
        talk("Increasing volume")
        volume_up()

    elif 'volume down' in command:
        talk("Decreasing volume")
        volume_down()

while True:
    run_assistant()