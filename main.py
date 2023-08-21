import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe() -> object:
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email id', 'password')
    server.sendmail('email id', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'C:\\my music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harsh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "emailid"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harsh bhai. I am not able to send this email")

        elif "temperature" in query:
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")

        elif "weather" in query:
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")

        elif "pause" in query:
            pyautogui.press("k")
            speak("video paused")
        elif "play" in query:
            pyautogui.press("k")
            speak("video played")
        elif "mute" in query:
            pyautogui.press("m")
            speak("video muted")

        elif "volume up" in query:
            from keyboard import volumeup
            speak("Turning volume up,sir")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown

            speak("Turning volume down, sir")
            volumedown()

        elif "remember that" in query:
            rememberMessage = query.replace("remember that", "")
            rememberMessage = query.replace("jarvis", "")
            speak("You told me to remember that" + rememberMessage)
            remember = open("Remember.txt", "a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            remember = open("Remember.txt", "r")
            speak("You told me to remember that" + remember.read())

        elif "news" in query:
            from NewsRead import latestnews

            latestnews()

        elif "shutdown the system" in query:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")

            elif shutdown == "no":
                break

        elif "screenshot" in query:
            import pyautogui

            im = pyautogui.screenshot()
            im.save("ss.jpg")

        elif "click my photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("SMILE")
            pyautogui.press("enter")

        elif "translate" in query:
            from Translator import translategl

            query = query.replace("jarvis", "")
            query = query.replace("translate", "")
            translategl(query)


