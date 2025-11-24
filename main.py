import speech_recognition as spr
import webbrowser as web
import pyttsx3
import musiclib
import subprocess
import time
import wikipedia

recognizer = spr.Recognizer()
engine=pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
for v in voices:
    if "female" in v.name.lower() or "zira" in v.name.lower():
        engine.setProperty('voice', v.id)
        break

engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wikipedia_search(query):
    try:
        speak("Searching on Wikipedia...")
        print("Searching on Wikipedia...")
        summary = wikipedia.summary(query, sentences=3)
        speak(summary)
        print(summary)
    except:
        speak("Sorry, I couldn't find information about that.")
        print("Sorry, I couldn't find information about that.")



def process_command(command):
    question_words = ["who", "what", "when", "how", "tell", "describe", "define", "explain", "why"]
    if any(command.startswith(q) for q in question_words):
        wikipedia_search(command)
        return
    if "open google" in command:
        web.open("https://google.com")

    elif "open youtube" in command:
        web.open("https://youtube.com")

    elif "open instagram" in command:
        web.open("https://instagram.com")

    elif "open linkedin" in command:
        web.open("https://linkedin.com")

    elif "open vtop bhopal" in command:
        web.open("https://vtop.vitbhopal.ac.in/vtop/open/page")
        
    elif "open vtop chennai" in command:
        web.open("https://vtopcc.vit.ac.in/vtop/open/page")
    
    elif command.startswith("play"):
        parts = command.split(" ")
        if len(parts) > 1:
            song = parts[1]
            if song in musiclib.music:
                web.open(musiclib.music[song])
            else:
                speak("Sorry, I can't find that song.")
                print("Sorry, I can't find that song.")
        else:
            speak("Please say a song name.")
            print("Please say a song name.")

    elif "open calculator" in command:
        subprocess.Popen("calc.exe")

    elif "open notepad" in command:
        subprocess.Popen("notepad.exe")

    elif "open command prompt" in command or "open cmd" in command:
        subprocess.Popen("cmd.exe")

    elif "shutdown" in command:
        subprocess.Popen("shutdown /s /t 1")

    elif "restart" in command:
        subprocess.Popen("shutdown /r /t 1")

    elif "lock" in command:
        subprocess.Popen("rundll32.exe user32.dll,LockWorkStation")
def listen_for_wake_word():
    with spr.Microphone() as source:
        print("Listening for wake word 'Lisa'...")
        try:
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=2)
            word = recognizer.recognize_google(audio)
            print("You said:", word)
            return word.lower()
        except:
            return ""
def active_mode():
    speak("Yes, I am listening. Say Lisa off to stop.")

    while True:
        with spr.Microphone() as source:
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio).lower()
                print("Command:", command)

                if "lisa off" in command or "stop listening" in command:
                    speak("Okay, going to sleep.")
                    break

                process_command(command)

            except:
                speak("Say the command again.")

if __name__ == "__main__":
    speak("Initializing Lisa...")

    while True:
        wake_word = listen_for_wake_word()

        if "lisa" in wake_word:
            active_mode()

