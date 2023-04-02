import openai
from apikey import api_data
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

from importlib.resources import path
from cv2 import split
import numpy as np
from PIL import Image
import pyautogui as p

'''
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime , QDate , Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from GUI import Ui_GUI

'''

openai.api_key=api_data

completion=openai.Completion()

def Reply(question):
    prompt=f'drone: {question}\n Jarvis: '
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Chando'], max_tokens=200)
    answer=response.choices[0].text.strip()
    return answer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
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

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)    
    server.ehlo()
    server.starttls()
    server.login('snehamaria012@gmail.com', 'snehadon')
    server.sendmail('snehamaria012@gmail.com', to, content)
    server.close()

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="1c7d34e340a84dc4b8f72720a88f803e"'

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")    

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

def TaskExcecution():
    p.press('esc')
    speak("verification sucessful")
    speak("Welcome back Sneha")



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
            npath = "C:\\Program Files \\notepad.exe"
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
                to = 'snehamaria012@gmail.com'
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
            speak("shutting down the system")
            os.system("shutdown /s /t 5") 

        elif 'restart the system' in query:
            speak("restarting the system")
            os.system("shutdown /r /t 5") 

        elif 'sleep the system' in query:
            speak("system going to sleep")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") 

        elif "tell me the news" in query:
            speak("please wait sir, feteching the latest news")
            news()               

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"miss, the time is {strtime}")

        elif "hello" in query:
            speak ("hello miss, may i help you with anything")

        elif "how are you" in query:
            speak ("i am fine, what about you")

        elif "i am also good" in query:
            speak ("thats great to hear from you")    

        elif "what are you doing" in query:
            speak ("waiting for your command")

    
                

               
        elif 'thank you' in query:
            speak ('Thanks for using me miss, have a good day')
            sys.exit()    

if __name__ == "__main__":

    recognizer = cv2.face.LBPHFaceRecognizer_create() 
    recognizer.read('trainer/trainer.yml')   
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) 

    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 2 


    names = ['','Sneha Maria'] 

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
    cam.set(3, 640) 
    cam.set(4, 480) 


    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)



    while True:

        ret, img =cam.read() 
        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) 

            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])
        
            if (accuracy < 100):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                TaskExcecution()

            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff 
        if k == 27:
            break


    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()            




        

          




        

