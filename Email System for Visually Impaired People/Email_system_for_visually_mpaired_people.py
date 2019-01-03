
from time import ctime
import time
import os
from gtts import gTTS
import smtplib
import webbrowser
import config
import speech_recognition as sr


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("start audio.mp3")


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Could not get you")
    except sr.RequestError as e:
        print("Network Issue; {0}".format(e))

    return data


def sophia(data):
    if "how are you" in data:
        speak("I am fine Ajay")

    if "what time" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Ajay, I will show you where " + location + " is.")
        webbrowser.open_new_tab("https://www.google.com/maps/place/" + location + "/&amp;")

    if "search" in data:
        google = input('Google search:')
        #google = recordAudio()
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' %google)

    if "mail" in data:
        speak("Subject of mail")
        subject = recordAudio()
        speak("Message")
        msg = recordAudio()
        def send_email(subject, msg):
            try:
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo()
                server.starttls()
                server.login(config.EMAIL_ADDRESS, config.PASSWORD)
                #sbjct = 'Subject : {}'.format(subject)
                #msgg = '{}'.format(msg)
                #message = '{}{}'.format(sbjct, msgg)
                message = '{} {}'.format(subject, msg)
                server.sendmail('Ajay', 'ajay19soni@gmail.com', message)
                server.quit()
                speak("Email sent!")
            except:
                speak("Email failed to send.")

        #subject = "Testing \n"
        #msg = "Hello there, how are you? This is state"

        send_email(subject, msg)



# initialization
time.sleep(2)
speak("Hi Ajay, I'm Sophia. What can I do for you?")
while 1:
    data = recordAudio()
    sophia(data)
