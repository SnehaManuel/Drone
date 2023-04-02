from http import server
from re import I
from urllib import request
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2 
import random
from requests import get
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import requests




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<12:
        speak(f"Good Morning!, its {tt}")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon!, its {tt}")    
    else:
        speak(f"Good Evening!, its {tt}")

    speak("I am Drone . how can i help you")  
def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8 )
 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:

        print("Say that again please...")  
        return "None" 
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)    
    server.ehlo()
    server.starttls()
    server.login('ibcslibrarian@gmail.com', 'beensneha')
    server.sendmail('ibcslibrarian@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True: 
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia... ')   
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open notepad" in query:
            npath = "C:\\Program Files (x86)\\notepad.exe"
            os.startfile(npath)    

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open engage' in query:
            webbrowser.open("https://yengage.yenepoya.edu.in/ilias.php?baseClass=ilrepositorygui&reloadpublic=1&cmd=frameset&ref_id=1")

        elif 'open google' in query:
            speak("What should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open commamd prompt' in query:
            os.system("start cmd")

        
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()    

        elif 'play music' in query:
            music_dir = "C:\\music"      
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd)) 

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif 'send a message on whatsapp' in query:
            speak ("What should i send ?")
            cm = takeCommand().lower()
            kit.sendwhatmsg("+919349395023","This is testing protocol",2,25)

        elif 'play  song on youtube' in query:
            kit.playonyt("i was never there")   

        elif "email to sneha" in query:
            try:
                speak("what should i say?") 
                content = takeCommand().lower()
                to = 'lbcslibrarian@gmail.com'
                sendEmail(to,content)
                speak("Email has been send") 

            except Exception as e:
                print(e) 
                speak("sorry sneha. i was not able to send the email") 

        

            #speak('do you have any other work')

        elif 'close camera' in query:
            speak('ok miss, closing camera')
            os.system("taskkill /f /im camera.exe")

        

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==13:
                music_dir = 'C:\\music' 
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0])) 

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5") 

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5") 

        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")            
               
        elif 'thank you' in query:
            speak ('Thanks for using me miss, have a good day')
            sys.exit()    




        

          




        

