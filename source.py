# Import the libraries
import os
import datetime
import wikipedia
import warnings
import webbrowser
import socket
import speedtest
import wolframalpha

from record import recordAudio
from response import assistantResponse
from wakeword import wakeWord
from greeting import greeting
from getdate import getDate
from getperson import getPerson
from getnews import getNews

# Ignore any warning messages
warnings.filterwarnings('ignore')

# Calling Functions
while True:

    # Record the audio
    text = recordAudio()
    response = ''

    # Check for the wake word/phrase
    if (wakeWord(text)) == True:

        # Check for greetings by the user
        response = response + greeting(text)

        # Tells you about her skills
        if('what are your skills' in text.lower()):
            word = 'Hi, I am alexis.  i can find location, Open a webpage, Answer your questions through' \
                   ' Google, Play songs, Tell you date and time, Check your Internet speed, Internet connection,' \
                   ' Do math calculations, Answers general knowledge questions, Cricket scores update,' \
                   ' News.'
            response = response + word

        # Check to see if the user said anything having to do with the date
        if('date' in text):
            get_date = getDate()
            response = response + greeting(text) +  ' ' + get_date

        # Check to see if user said anything having to do with time
        if('time' in text):
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >=21:
                meridiem= 'p.m'
                hour = now.hour - 12
            else:
                meridiem = 'a.m'
                hour = now.hour

            # Convert minute into a proper string
            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)

            response = response + greeting(text) + ' ' + 'It is ' + str(hour) + ' : ' + minute + ' ' + meridiem+ '.'

        # Check to see if the user said 'who is'
        if ('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences = 2)
            response = response + ' ' + wiki

        # Opens a webpage
        if ('open' in text.lower()):
            response = response + 'Opening now'
            url = text[12:]+".com"
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)

        # Runs Visual Code Studio
        if ('run visual code studio' in text.lower()):
            codePath = "C:/Users/HP/Desktop/Microsoft VS Code/Code.exe"
            os.startfile(codePath)

        # Runs command prompt
        if ('run command prompt' in text.lower()):
            os.system('start cmd /k "Your Command Prompt Command"')
            # response = response + 'Opening command prompt'

        # Plays music from the music library on your laptop
        if ('play music' in text.lower()):
            songs_dir = "E:/Music"
            songs = os.listdir(songs_dir)
            print(songs)
            response = os.startfile(os.path.join(songs_dir, songs[0]))

        # Searches you anything from google
        if ('i want to search' in text.lower()):
            print('What can i search for you ?')
            search = recordAudio()
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            response = response + 'Searching ' +  search

        # Calculates anything for you
        if ('calculate for me' in text.lower()):
            print('What can i calculate for you ?')
            question = recordAudio()
            app_id = "ENTER-YOUR-API-KEY"

            # Instance of wolf ram alpha client class
            client = wolframalpha.Client(app_id)

            # Stores the response from wolfram alpha
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            response = response + answer

        # Finding the location
        if ('find me a location' in text.lower()):
            print('What is the location ?')
            location = recordAudio()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            response = 'Here is the location of ' + location

        # Checking internet connection
        if ('check internet connection' in text.lower()):
            IPaddress = socket.gethostbyname(socket.gethostname())
            if IPaddress == "127.0.0.1":
                response = response + "No internet, your localhost is " + IPaddress
            else:
                response = response + "Connected, with the IP address: " + IPaddress

        # Checking the internet speed
        if ('what is the internet speed' in text.lower()):
            st = speedtest.Speedtest()
            response = response + "Download Speed: " + str(st.download())
            response = response + "Upload Speed: " + str(st.upload())
            response = response + "Ping Speed: " + str(st.ping())

         # Tells you current news from BBC News
        if ("tell me today's news" in text.lower()):
            getnews = getNews()
            response = response + ' ' +  str(getnews)

        # Exit Command
        if ('exit' in text.lower()):
            exit()

        # Have the assistant respond back using audio and text from response
        assistantResponse(response)