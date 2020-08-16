![](https://img.shields.io/badge/git-fff7f8?colorA=faf0f0&colorB=db4823&style=for-the-badge&logo=git)
![](https://img.shields.io/badge/github-fff7f8?colorA=080808&colorB=8a8a8a&style=for-the-badge&logo=github)
![](https://img.shields.io/badge/for-you-099450?colorA=b0c92e&colorB=487d3e&style=for-the-badge)
![](https://img.shields.io/badge/python-used-bee5ed?colorA=37b6bd&colorB=3c9bb5&style=for-the-badge&logo=python)
![](https://img.shields.io/badge/visual_studio_code-1.47.3-181717?colorA=ae36d6&style=for-the-badge&logo=visual-studio-code)
# :small_orange_diamond: credentials.json :warning:
### For getting access from Google Contacts using Gmail API :busts_in_silhouette:
After generating Gmail API, the ```CLIENT CONFIGURATION``` will be saved as ***```credentials.json```***. It ***```should be kept in the working directory```***. otherwise contacts details can't be fetched from Google Contacts.
# :small_orange_diamond: token.pickle :memo:
All the details will be saved in ***```token.pickle```*** file and no further retrieving will be occurred if there is no change.
# :small_orange_diamond: contact.py :ledger:
### Simple program for retrieving contact details from Google Contacts using Gmail API :bust_in_silhouette: :e-mail: :calling:
##### All the necessary steps for retrieving the contact details from Google Contacts are following -
:small_blue_diamond: One'll need to get the ```CLIENT CONFIGURATION``` as ***```credentials.json```*** file using ***```Gmail API```***. It should be kept in the **working directory** for functioning. <br><br>
:small_blue_diamond: While generating the ```CLIENT CONFIGURATION``` one'll need to give a project name. Please note that ```this project name and the main python```<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```program name should be same```. <br><br>
:small_blue_diamond: One'll need to then install Google **Client Library** via pip - <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```<br><br>
