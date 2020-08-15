from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']

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
    

def fetchNamePhoneNo():
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
    return namePhoneNoList


if __name__ == "__main__":
    zippedNameEmailList = fetchNameEmail()
    name1List, emailList = zip(*zippedNameEmailList)
    # i = 1
    # for item in name1List:
    #     print(f"{i} {item}")
    #     i+=1
    # i = 1
    # for item in emailList:
    #     print(f"{i} {item}")
    #     i+=1
    zippednamePhoneNoList = fetchNamePhoneNo()
    name2List, phoneNoList = zip(*zippednamePhoneNoList)
    i = 1
    for item in name2List:
        print(f"{i} {item}")
        i+=1
    i = 1
    for item in phoneNoList:
        print(f"{i} {item}")
        i+=1
    # queryList = ["Send", "a", "mail", "to", "Amit"]
    # i = 0
    # for item1 in name1List:
    #     for item2 in queryList:
    #         if item2 == item1:
    #             print(f"No - {i+1}\nitem1-{item1}\nitem2-{item2}")
    #             break
    #     i+=1
    # if i+1 > len(name1List):
    #     print(f"Item not found\nj={i+1}")