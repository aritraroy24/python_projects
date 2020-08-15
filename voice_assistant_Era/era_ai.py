from __future__ import print_function
import pyttsx3
import datetime
import smtplib
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from twilio.rest import Client
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests
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
    elif hour >= 18 and hour < 23:
        speak("Good Evening!")
    else:
        speak("Good Night, sir...It's good for health to have dinner and go to bed now...as you know Early to bed and early to rise, makes a man healthy, wealthy and wise.")
        speak("Thanks for using Era")
        exit()
        
    speak("I'm Era, your personal voice assistant. Please tell how may I help you?")

def sendEmail(to, content):
    # It sends an email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com',
                 'your_password')    # Enter your password
    server.sendmail('your_email@gmail.com', to, content)
    server.close()


def fetchNameEmail():
    """Fetches name and their email ids from google contacts"""
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
    sortedName1List = sorted(nameEmailList, key = lambda x: x[0]) 
    return sortedName1List
    

def name1Lower(name1List):
    """Makes all the names lowercase for name-email id list"""
    name1ListLowerSplit = []
    name1ListLower = list(map(lambda x:x.lower(), name1List))
    name1ListLowerSplit = list(map(lambda x: x.split(), name1ListLower))
    return name1ListLowerSplit

def fetchNamePhoneNo():
    """Fetches name and their phone numbers from google contacts"""
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
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=1500,
        personFields='names,emailAddresses,phoneNumbers').execute()
    connections = results.get('connections', [])

    name2List = []
    phoneNoList = []
    for person in connections:
        names = person.get('names', [])
        phones = person.get('phoneNumbers', [])

        if phones:
            name = names[0].get('displayName')
            name2List.append(name)
            phone = phones[0]['value']
            phoneNoList.append(phone)
    namePhoneNoList = zip(name2List, phoneNoList)
    sortedName2List = sorted(namePhoneNoList, key = lambda x: x[0])
    return sortedName2List

def name2Lower(name2List):
    """Makes all the names lowercase for name-phone number list"""
    name2ListLowerSplit = []
    name2ListLower = list(map(lambda x:x.lower(), name2List))
    name2ListLowerSplit = list(map(lambda x: x.split(), name2ListLower))
    return name2ListLowerSplit

def queryLowerSplit(query):
    """Makes all the query elements lowercase"""
    queryLower = query.lower()
    lst = []
    lst = queryLower.split()
    return lst

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


def givenews():
    speak("News for today..Lets begin")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=cbdbe6b492824c9b837b508c4d0fdc92"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    i = 1
    for article in arts[:-1]:
        speak(article['title'])
        print(f"\n{i}. {article['title']}")
        speak("Moving on to the next news....")
        i+=1
    for article in arts[-1:]:
            speak(article['title'])
            print(f"\n{i}. {article['title']}")
            speak("Thanks for listening...")
    speak("Stay tuned for more updated news")


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

        elif 'quit' in query or 'exit' in query or 'close' in query:
            speak("Thanks for using Era!!!")
            exit()

        elif 'awesome' in query or 'wow' in query or 'amazing' in query or 'wonderful' in query:
            speak("Thank you sir, I'm always here for you")

        elif 'what' in query or 'who' in query or 'where' in query or 'can you' in query:
            webbrowser.open(f"https://www.google.com/search?&q={query}")
            speak(wikipedia.summary(query, sentences=2))

        elif 'email to' in query or 'send a mail' in query or 'mail to' in query:
            # This will send mail only if there is any matching name in last of query
            # the last word should be in all strings contain a name which is exist as key in nameList
            zippedNameEmailList = fetchNameEmail()
            name1List, emailList = zip(*zippedNameEmailList)
            name1FinalList = name1Lower(name1List)
            queryList = queryLowerSplit(query)
            i = 0
            for item in name1FinalList:
                i+=1
                for item1 in item:
                    for item2 in queryList:
                        if item2 == item1:
                            try:
                                speak("What is your message ?")
                                content = takeCommand()
                                to = emailList[i-1]
                                sendEmail(to, content)
                                speak("Email has been sent")
                                break
                            except Exception as e:
                                print(e)
                                speak("Sorry sir, something went wrong and i am not able to send your email right now.")
                                break
                    else:
                        continue
                    break
                else:
                    continue
                break
            if i+1 > len(name1FinalList):
                speak("Contact not found")

        elif 'phone' in query or 'make call' in query or 'call' in query:
            zippednamePhoneNoList = fetchNamePhoneNo()
            name2List, phoneNoList = zip(*zippednamePhoneNoList)
            name2FinalList = name2Lower(name2List)
            queryList = queryLowerSplit(query)
            i = 0
            for item in name2FinalList:
                i+=1
                for item1 in item:
                    for item2 in queryList:
                        if item2 == item1:
                            try:
                                # Your Account Sid and Auth Token from twilio.com/console
                                # DANGER! This is insecure. See http://twil.io/secure
                                account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                                auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                                client = Client(account_sid, auth_token)

                                call = client.calls.create(
                                                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                                                        to = phoneNoList[i-1],
                                                        from_='+1XXXXXXXXXX'
                                                    )
                                speak("Calling has been initiated")
                                break
                            except Exception as e:
                                print(e)
                                speak("Sorry sir, something went wrong and i am not able to call right now.")
                                break
                    else:
                        continue
                    break
                else:
                    continue
                break
            if i+1 > len(name2FinalList):
                speak("Contact not found")

        elif 'headlines' in query or 'news' in query or 'headline' in query:
            givenews()