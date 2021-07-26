import random
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour <= 12:
        speak('Good Morning, Sir')

    elif 12 <= hour <= 17:
        speak('Good Afternoon, Sir')

    elif 18 <= hour <= 22:
        speak('Good Evening, Sir')

    speak('I am Jarvis Sir, Please Tell Me How May I Help You.')


def takeCommand():
    # It takes microphone input from the user and returns the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
        speak(query)

    except Exception as e:
        engine.say('Sorry Sir, I am Unable to Get That, Please Say That Again Clear And Loud.')
        return None

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anshulgupta96626@gmail.com', 'starbharat1212')
    server.sendmail('anshulgupta96626@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic For Executing Task Based On Query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak(f'According to wikipedia {results}')
            print(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play video' in query:
            video_dir = 'E:\\MOVIES\\WEB SERIES\\DELHI CRIME'
            videos = os.listdir(video_dir)
            num = random.randint(1, 7)
            os.startfile(os.path.join(video_dir, videos[num]))

        elif 'play music' in query:
            music_dir = 'C:\\Users\\anshu\\OneDrive\\Desktop\\course file\\java script projects\\music player\\music'
            music = os.listdir(music_dir)
            num = random.randint(1, 6)
            os.startfile(os.path.join(music_dir, music[num]))

        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir The Time Is, {time}")

        elif 'open visual studio' in query:
            vs = '"C:\\Users\\anshu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(vs)

        elif 'jarvis quit' in query:
            speak('Ok Sir, i am Going On Sleep mode. Have a nice day ahead sir.')
            break
