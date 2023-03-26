import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
from datetime import date
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('I am Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Wolfpack' in command:
                command = command.replace('Wolfpack', '')
                print(command)
    except:
        pass

    return command


def run_wolfpack():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'current time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)

    elif 'date' in command:
        today = date.today()
        date1 = today.strftime("%B %d, %Y")
        print('Today\'s date is ' + date1)
        talk('Today\'s date is ' + date1)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'Are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.')


while True:
    run_wolfpack()
