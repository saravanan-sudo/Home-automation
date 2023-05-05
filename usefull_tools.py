import pywhatkit
import pyttsx3
import wikipedia
import datetime
import pyjokes


def talk(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def utilites(command):
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing the '+song + 'in Youtube')
        pywhatkit.playonyt(song)
        exit()
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print('Current time is ' + time)
        exit()
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        exit()
    elif 'date' in command:
        talk('sorry, I have a headache')
        exit()
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
        exit()
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        exit()
    else:
        talk('Please say the command again.')
        exit()
