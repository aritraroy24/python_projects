from __future__ import print_function
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']


def speak(audio):
    # It speaks a given string
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    # Wish according to the time.
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour < 20:
        speak("Good Evening!")
    else:
        speak("Good Night, sir...It's good for health to have dinner and go to bed now...as you know Early to bed and early to rise, makes a man healthy, wealthy and wise.")
        speak("Thanks for using Era, sir!!!")
        exit()
        
    speak("I'm Era, your personal voice assistant. Please tell how may I help you?")


def fetchNameEmail():
    """Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('people', 'v1', credentials=creds)

    # Call the People API
    print('List of all name with email id and phone number:\n')
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=1500,
        personFields='names,emailAddresses').execute()
    connections = results.get('connections', [])
    name1List = []
    emailList = []
    for person in connections:
        names = person.get('names', [])
        emails = person.get('emailAddresses', [])

        if names and emails:
            name = names[0].get('displayName')
            name1List.append(name)
            email = emails[0]['value']
            emailList.append(email)
    nameEmailList = zip(name1List, emailList)
    return nameEmailList
    

def fetchPhoneNo():
    """Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('people', 'v1', credentials=creds)

    # Call the People API
    print('List of all name with email id and phone number:\n')
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=1500,
        personFields='names,emailAddresses,phoneNumbers').execute()
    connections = results.get('connections', [])

    nameList = []
    emailList = []
    phoneNoList = []
    for person in connections:
        names = person.get('names', [])
        phones = person.get('phoneNumbers', [])

        if names and phones:
            name = names[0].get('displayName')
            nameList.append(name)
            phone = phones[0]['value']
            phoneNoList.append(phone)
    

def takeCommand():
    # It takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=4)  # it converts the audio input into string and gives a span of 4 sec to an user to speak

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # query = r.recognize_sphinx(audio)     #instead of that we can use this is offline but accuray very poor
        print(f"User said: {query}")
    except:
        print("Say that again please...")
        return "None"
    return query

def splitWords(query):
    return (lst[0].split()) 

if __name__ == '__main__':
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "how are you" in query:
            speak("I'm fine sir, what about you?")
        elif "fine" in query:
            speak("It's good to know that you are fine.")
        elif "who are you" in query:
            speak("My name is Era. I'm a desktop assistant made by Mr Aritra.")
        elif 'wikipedia' in query:
            # sentences=2 means return first two string
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            # print("According to wikipedia")
            # print(results)
            speak(results)
        elif 'open spartan' in query or 'spartan' in query:
            spartanPath = "C:\\Program Files\\Wavefunction\\Spartan14v114\\WF14gui64.exe"
            os.startfile(spartanPath)
        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')
        elif 'open google' in query:
            webbrowser.open('https://www.google.co.in/')
        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com/')
        elif 'play music' in query or 'play song' in query or 'play some music' in query or 'play another music' in query or 'change song' in query or 'next song' in query:
            music_dir = 'G:\\RabindraSangeet'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(
                music_dir, songs[random.randint(0, len(songs)-1)]))
        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query or 'open visual studio' in query:
            codePath = "C:\\Users\\Aritra Roy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'jarvis quit' in query or 'exit' in query or 'close' in query:
            speak("Thanks for using Era!!!")
            exit()

        elif 'awesome' in query or 'wow' in query or 'amazing' in query or 'wonderful' in query:
            speak("Thank you sir, i am always here for you")

        elif 'what' in query or 'who' in query or 'where' in query or 'can you' in query:
            webbrowser.open(f"https://www.google.com/search?&q={query}")
            speak(wikipedia.summary(query, sentences=2))

        elif 'email to' in query or 'send a mail' in query or 'mail to' in query:
            # This will send mail only if there is any matching name in last of query
            # the last word should be in all strings contain a name which is exist as key in nameList
            name1List, emailList = zip(*zippedNameEmailList)
            queryList = splitWords(query)
            i = 0
            for item1 in name1List:
                for item2 in queryList:
                    if item2 == item1:
                        break
                i+=1