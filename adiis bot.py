from winreg import QueryInfoKey
from django.http import QueryDict
import pyttsx3
from requests import get
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import cv2
import requests
import pywhatkit
import sys
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) for male voice
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18: 
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am Aditya's bot.  Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak
        ("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()





if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query=takeCommand().lower()

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
            speak("sir , what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir= 'C:\adity \Music'
            songs = os.listdir("music-dir")
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to aditya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "adityakumar824312@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my I am not able to send this email")  
        #for camera
        elif 'open camera' in query:
            speak (f'ok sir wait   opening  camrea')
            cap = cv2.videocapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow ("videocapture",img)
                k = cv2.waitKeyEx
                if k==30:
                    break
            cap.release()
            #ip address
        elif 'ip address'in query:
            Ip = get('https://api.ipify.org').text
            speak (F"your ip address is {Ip}")

            #for google
        elif 'open google'in query:
           speak ("sir ,what should i search on google")

        elif 'ok bye' in query:
            speak("thanks for using me have a good day")

        elif 'tell me about Alok' in query:
            speak ("she is a little piggy")

        elif 'who are my brothers' in query:
            speak("oaky sir ")
            speak(" two brothers" )
        elif 'no thanks' in query:
             speak ("thanks for using me sir, have a nice day")
             sys.exit()
        speak("sir, do you have any another work")
        
        #elif( 'where I am ' )in query:'where we are ' in query:
        #speakpeak ("wait sir , let me check  ")
