![](https://img.shields.io/badge/git-fff7f8?colorA=faf0f0&colorB=db4823&style=for-the-badge&logo=git)
![](https://img.shields.io/badge/github-fff7f8?colorA=080808&colorB=8a8a8a&style=for-the-badge&logo=github)
![](https://img.shields.io/badge/for-you-099450?colorA=b0c92e&colorB=487d3e&style=for-the-badge)
![](https://img.shields.io/badge/python-used-bee5ed?colorA=37b6bd&colorB=3c9bb5&style=for-the-badge&logo=python)
![](https://img.shields.io/badge/visual_studio_code-1.51.1-181717?colorA=ae36d6&style=for-the-badge&logo=visual-studio-code)
## :small_orange_diamond: WAppBot.py :robot:
##### A python script for sending ***Good Morning*** (at *7 AM*) and ***Good Night*** (at *11:30 PM*) messages to selected contacts.
## :small_orange_diamond: chromedriver.exe
This applicaion is necessary for running the application in windows.
## :small_orange_diamond: contact.txt :closed_book:
List of the selected contacts for sending messages.
## :small_orange_diamond: morningMsg.txt :pencil:
List of 20 different Good Morning messages for sending random Good Morning messages.
## :small_orange_diamond: nightMsg.txt :pencil:
List of 20 different Good Night messages for sending random Good Night messages.

----
## Used Modules
:small_red_triangle: ***selenium*** <br>
:small_red_triangle: ***time*** <br>
:small_red_triangle: ***datetime*** <br>
:small_red_triangle: ***random*** <br>
## Process: :point_down:
#### All the necessary steps for retrieving the contact details from Google Contacts are following -
:small_blue_diamond: **```Fork```** and **```Star```** the repository. **Clone** it to make your own local copy. <br><br>
:small_blue_diamond: Install the **selenium module** using ***```pip install selenium```*** and navigate to your folder. <br><br>
:small_blue_diamond: Put your contacts in the [**```contact.txt```**](https://github.com/aritraroy24/python_projects/blob/master/WhatsAppBot/contact.txt) file [Do it in your local copy] and change the file name to ***```contact.txt```*** in the code in line no. **42** <br><br>
:small_blue_diamond: You can add or change **Good Morning** messages or **Good Night** messages by modifying ***morningMsg.txt*** file or ***nightMsg.txt*** <br><br>

----
#### :warning: You have to ```scan the QR Code``` for starting WhatsApp Web using your phone while starting the application.
#### :warning: You have to ```set the xpath``` (in line no. **57** and line no. **60**) by using Chrome Developer options.
#### :warning: If you are using ```Mac``` or ```Linux``` please use the ```appropriate Chromedriver application``` using [this link](https://chromedriver.storage.googleapis.com/index.html?path=87.0.4280.20/).
