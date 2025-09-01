'''import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(text)
    engine.runAndWait() 

def input():
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        print("  Listening...")
        recogniser.pause_threshould = 1
        audio = recogniser.listen(source)

        try:
            command = recogniser.recognize_google(audio,language='en-in')
            print("You said : ",command)
            return command.lower()
        except sr.UnknownValueError:
            print("❌, I didn't understand that")
            speak("❌, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Speech service error.")
            speak("Sorry, my speech service is down.")
            return ""

speak("Hello! I'm your virtual assistant. How can I help you?")
while True:
    command = input()
    if 'play music' in command:
        speak('okay, Music is playing')
        print("yah! i am playing...")
    elif 'alarm' in command:
        speak('okay ! I Have set up alarm')'''
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

engine = pyttsx3.init()

def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # 0 = male voice, 1 = female (depends on system)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='en-in')
            print("👉 You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("❌ I didn’t understand that.")
            speak("Sorry, I didn’t catch that.")
            return ""
        except sr.RequestError:
            print("⚠️ Speech service error.")
            speak("Sorry, my speech service is down.")
            return ""

# Start Assistant
speak("Hello! I'm your virtual assistant. How can I help you?")

while True:
    command = take_command()

    if 'play music' in command:
        speak("Okay! Playing music now.")
        print("🎶 Music is playing...")
        # Example: Play a music file if available
        music_path = r"C:\Users\chait\Downloads\[iSongs.info] 03 - Don u Don u Don u.mp3"
        if os.path.exists(music_path):
            os.startfile(music_path)

    elif 'open google' in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")

    elif 'open youtube' in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif 'time' in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")
        print("🕒 Current Time:", now)

    elif 'date' in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today is {today}")
        print("📅 Today's Date:", today)

    elif 'alarm' in command:
        speak("Okay, I will remind you soon! But I don't have a real alarm yet.")
        print("⏰ Alarm feature not fully implemented!")

    elif 'exit' in command or 'quit' in command or 'stop' in command:
        speak("Goodbye! Have a great day.")
        print("👋 Assistant stopped.")
        break

    elif command != "":
        speak("Sorry, I don’t know that command yet.")
        print("⚠️ Unknown command:", command)
