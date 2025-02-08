import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
from tkinter import *

# Initialize the Tkinter window
Faizan_root = Tk()
Faizan_root.geometry("300x400")
Faizan_root.title("JARVIS AI by Faizan Jallani")

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Define the wake word
WAKE = "hey jarvis"

def speak(audio):
    """Function to speak the given audio."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Function to greet the user based on the time of the day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am JARVIS. How may I help you Sir?")

def takeCommand():
    """Function to take voice command from the user."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def get_audio():
    """Function to get audio input from the user."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language='en-in')
        print(f"User said: {text}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return text

def main():
    """Main function to handle the logic of the assistant."""
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query.
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/", new=2)
            speak("Enjoy")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/", new=2)

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/", new=2)

        elif 'play music' in query:
            music_dir = 'F:\\songs\\Favorite'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Faizan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/", new=2)

        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/faizangujjar01/", new=2)
            speak("Have a look sir")

        elif 'are you there' in query:
            stMsgs = ['At your service, Sir']
            speak(stMsgs[0])

        elif 'what is' in query or 'search for' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'shutdown the pc' in query:
            choice = input("Please confirm to shutdown the pc (y or n): ")
            if choice == 'n':
                exit()
            else:
                os.system("shutdown /s /t 1")

        elif 'exit' in query:
            speak("Ok sir, Take Care.")
            sys.exit()

if __name__ == '__main__':
    main()
    Faizan_root.mainloop()