from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import random

path = "F:\Programming\GitHub\python_projects\WhatsAppBot"
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

time.sleep(12)

def msgLower(msglist):
    """Makes all the messages lowercase for message-list"""
    msgListLowerSplit = []
    msgListLower = list(map(lambda x:x.lower(), msglist))
    msgListLowerSplit = list(map(lambda x: x.split(), msgListLower))
    return msgListLowerSplit

def morningMsgList():
    morningMsgFile = open('morningMsg.txt', "r") #opens the file morningMsg.txt in read mode
    morningList = morningMsgFile.read().splitlines() #puts the file into an array
    morningMsgFile.close()
    # print(morningList)
    finalMorningMsg = random.choice(morningList)
    return finalMorningMsg

def nightMsgList():
    nightMsgFile = open('nightMsg.txt', "r") #opens the file nightMsg.txt in read mode
    nightList = nightMsgFile.read().splitlines() #puts the file into an array
    nightMsgFile.close()
    # print(nightList)
    finalNightMsg = random.choice(nightList)
    return finalNightMsg

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file contacts.txt in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words
names = readFile('contacts.txt')  # Create a contact.txt file in same folder

if __name__ == '__main__':
    while True:
        timeThen = str(datetime.now().strftime('%H:%M:%S'))
        
        if timeThen == "07:00:00":
            for name in names:
                try:
                    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                    person.click()

                    for i in range(1,3):
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    msg_got = driver.find_elements_by_xpath('//div[@class="_1RAno message-out focusable-list-item"]//div//div//div//div//div//span[@class="_1VzZY selectable-text invisible-space copyable-text"]')
                    msglist = [message.text for message in msg_got]

                    day_check = driver.find_elements_by_xpath('//div[@class="_1ij5F KpuSa"]//span[@dir="auto"][@class="_1VzZY"]')
                    day = [days.text for days in day_check]
                    msgLowerList = msgLower(msglist)

                    try:
                        msgFinalList = msgLowerList[-1]
                        # print(msgFinalList)
                        flag = 0
                        for msgWord in msgFinalList:
                            if msgWord == "morning":
                                flag = 1
                                break
                        if flag == 0 and day != "TODAY":
                            reply = driver.find_element_by_xpath('//div[@data-tab="6"]')
                            reply.clear()
                            reply.send_keys(f"{morningMsgList()}")
                            reply.send_keys(Keys.RETURN)
                            print(f"Sent to {name}")
                        else:
                            print(f"Already sent to {name}")
                    except:
                        print("Array length problem...")
                        pass
                except:
                    print("Something went wrong...")
                    pass
        
        elif timeThen == "23:30:00":
            for name in names:
                try:
                    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                    person.click()

                    for i in range(1,3):
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    msg_got = driver.find_elements_by_xpath('//div[@class="_1RAno message-out focusable-list-item"]//div//div//div//div//div//span[@class="_1VzZY selectable-text invisible-space copyable-text"]')
                    msglist = [message.text for message in msg_got]

                    day_check = driver.find_elements_by_xpath('//div[@class="_1ij5F KpuSa"]//span[@dir="auto"][@class="_1VzZY"]')
                    day = [days.text for days in day_check]
                    msgLowerList = msgLower(msglist)

                    try:
                        msgFinalList = msgLowerList[-1]
                        flag = 0
                        for msgWord in msgFinalList:
                            if msgWord == "night":
                                flag = 1
                                break
                        if flag == 0 and day != "TODAY":
                            reply = driver.find_element_by_xpath('//div[@data-tab="6"]')
                            reply.clear()
                            reply.send_keys(f"{nightMsgList()}")
                            reply.send_keys(Keys.RETURN)
                            print(f"Sent to {name}")
                        else:
                            print(f"Already sent to {name}")
                    except:
                        print("Array length problem...")
                        pass
                except:
                    print("Something went wrong...")
                    pass