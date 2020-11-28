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
    morningList = ["Good Morning ... ",
                "Good Morning ...❤️❤️❤️", 
                "Good Morning ...Have a nice day ...", 
                "Today is the future that we worried about yesterday. See, it’s not so bad. Here’s to a happy day.",
                "Nothing is impossible when God is on your side. Good morning ...", 
                "DREAMING or DOING is a choice that will mean the difference between FAILURE or SUCCESS. Good morning ...",
                "Wake up every morning with the thought that something wonderful is about to happen. Good Morning ...",
                "May rays of the morning sun light the fire in you to achieve big things in life. Good morning ...",
                "Every morning gives each one of us 24 hours to fulfil our dreams. It’s just who is using that time the best possible way. Good Morning ...",
                "No matter what, the morning is always beautiful. Embrace it to feel its beauty. Good Morning ...",
                "Sunrises are the best; enjoy a cup of coffee or tea with yourself because this day is yours, good morning !!!  Have a wonderful day ahead.",
                "A great end may not be decided but a good creative beginning can be planned and achieved. Good morning ... have a productive day!",
                "I like the sunrises more than sunsets, they make me dream about us all day. Good Morning ...",
                "Morning is not only sunrise but A Beautiful Miracle of God that defeats the darkness and spread light. Good Morning ...",
                "Life never gives you a second chance. So, enjoy every bit of it. Why not start with this beautiful morning. Good Morning !!!",
                "If you want to gain health and beauty, you should wake up early. Good Morning !!!",
                "Nothing is in your hand except your Karma. Do good without any hope and desire. Good Morning ...",
                "Accept the bouquet of flower. I know it won’t solve your problem, but it will give you a great start. Good Morning ...",
                "Enjoy these moments now because they don't last forever. Good Morning ...",
                "Start Your day with the sweetest smile. Good Morning"]
    finalMorningMsg = random.choice(morningList)
    return finalMorningMsg

def nightMsgList():
    nightList = ["Always end the day with a positive thought and grateful heart. Good Night !!!",
                "If someone wishes you good night every day, You’re happier than so many people. Happy Good Night ...",
                "I like the night. Without the dark, we’d never see the stars.Happy Good Night ...",
                "Anything seems possible at night when the rest of the world has gone to sleep. Good Night",
                "Please don’t let a bad day convince you that you have a bad life. Good Night !!!",
                "May the night fill with stars for you. May counting every one, give you contentment!",
                "Good night ... Have a sweet dream... ❤️❤️❤️",
                "If you’re tired learn to rest, not quit. Good Night ...",
                "As the day comes to an end, throw all your worries and troubles away. Have a blissful night full of beautiful dreams.",
                "May your pillow be soft, and your rest be long! Good night ...",
                "After an exhausting day, it is only fair that we have a sweet sleep. Have a magical night and sweet dreams. Good night.",
                "May the stars and the moon comfort you as you sleep. Good night and have sweet dreams.",
                "Good night ... May you have sweet dreams tonight.",
                "I pray your sleep is accompanied by sweet dreams. Good night ...",
                "Darkness cannot last forever. Keep the hope alive. Good night ...",
                "Wishing you a good night where you can recharge for tomorrow!",
                "Have a night that is noiseless and comfortable...",
                "May the dreams you have tonight, come true tomorrow! You can do anything that is on your mind and in your heart! Good Night ...",
                "Sleep your worries away tonight, for tomorrow will be better. Have a good night ...",
                "Studies have shown that having a good night’s sleep has the ability to drastically wipe away our worries and fears. So sleep tight and have pleasant dreams. Good Night ..."]
    finalNightMsg = random.choice(nightList)
    return finalNightMsg

names = ["Aritra (Airtel)", "Uchche - 1", "Arpita (PU-1)"]

if __name__ == '__main__':
    while True:
        # t1 = str(datetime.now())
        # timeThen = datetime.strptime(t1, '%Y-%m-%d %H:%M:%S.%f').strftime('%H:%M:%S')
        timeThen = str(datetime.now().strftime('%H:%M:%S'))
        
        if timeThen == "07:00:00":
            for name in names:
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
                    print(msgFinalList)
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
                    print("Something went wrong...")
        
        elif timeThen == "23:30:00":
            for name in names:
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
                    print("Something went wrong...")