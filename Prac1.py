import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Customize the voice (optional)
def configure_voice():
    """Configure the voice settings for the TTS engine."""
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change to a male voice (if available)
    engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)

def speak(text):
    """Convert text to speech and play it."""
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def recognize_speech_from_microphone():
    """Listen to the microphone and recognize speech."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio).lower()
        print("Recognized Text from microphone:", text)
        return text
    except sr.UnknownValueError:
        speak("I didn't catch that. Could you please repeat?")
        return None
    except sr.RequestError as e:
        speak("Sorry, I am having trouble accessing the speech recognition service.")
        print(f"Error: {e}")
        return None

def generate_response(text):
    """Generate a response based on the recognized text."""
    if text == "hello":
        return "Hello Sir, How are you?"
    elif text in ["bye", "exit", "quit"]:
        return "Goodbye Sir! Have a great day!"
    elif "how are you" in text:
        return "I'm just a program, but I'm functioning perfectly. How can I assist you?"
    elif "your name" in text:
        return "I am your personal assistant."
    elif "time" in text:
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."
    else:
        return f"You said: {text}"

def main():
    """Main function to run the speech recognition and response system."""
    print("Speech Recognition Version:", sr.__version__)
    configure_voice()  # Configure voice settings
    speak("Initializing your personal assistant. How can I help you today?")

    while True:
        text = recognize_speech_from_microphone()
        if text:
            response = generate_response(text)
            speak(response)
            if text in ["bye", "exit", "quit"]:
                break  # Exit the loop if the user says "bye" or "exit"

if __name__ == "__main__":
    main()