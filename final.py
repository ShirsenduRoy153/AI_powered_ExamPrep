import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('shirsendu.roy.15032002@gmail.com', 'hgeurghwilioosba')
    server.sendmail('shirsendu.roy.15032002@gmail.com','shirsenduroy153@gmail.com','hello run hello')


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        talk("Please say the command again")
        take_command()
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'what is a' in command:
        object = command.replace('what is a', '')
        info = wikipedia.summary(object, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
        print('sorry I have a headache')
    elif 'send mail' in command:
        mail()
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'best teacher' in command:
        talk('best teacher in STCET is our LATIB SIR')
        print('best teacher in STCET is our LATIB SIR')
        run_alexa()
    else:
        talk('Please say the command again.')
        run_alexa()

run_alexa()