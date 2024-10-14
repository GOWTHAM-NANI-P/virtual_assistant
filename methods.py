import datetime
import pyttsx3
import pywhatkit
import pyautogui
import speech_recognition as sr
import wikipedia

r=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(command):
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("listening...")
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print(my_text)
            return my_text
    except:
        print("no speech detected")
        return None

def time():
    tim=datetime.datetime.now().strftime('%H:%M')
    print(tim)
    speak(tim)

def date():
    today=datetime.date.today()
    print(today)
    #speak('today the date is'+str(today))
    speak(today)
    
def yt():
    my_text = my_text.replace('play', '').strip()
    speak('playing'+my_text)
    pywhatkit.playonyt(my_text)

def volume(my_text):
    if 'mute' in my_text:
        pyautogui.press("volumemute")
    elif 'unmute' in my_text:
        pyautogui.press("unmute")
    elif 'increase' in my_text and 'more' in my_text:
        speak("increasing more volume sir")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
    elif 'increase' in my_text:
            speak("increasing volume sir")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
    elif 'decrease' in my_text and 'more' in my_text:
        speak("decreasing more volume sir")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
    else:
        speak("decreasing volume sir")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown") 

def msgmg(ms):
    pywhatkit.sendwhatmsg_instantly("+919704030021", ms)
def msgme(ms):
    pywhatkit.sendwhatmsg_instantly("+919182524219", ms)
def msgmh(ms):
    pywhatkit.sendwhatmsg_instantly("+917673913754", ms)
def msgsj(ms):
    pywhatkit.sendwhatmsg_instantly("+917416936298", ms)
def msgsk(ms):
    pywhatkit.sendwhatmsg_instantly("+919381922191", ms)
def msgna(ms):
    pywhatkit.sendwhatmsg_instantly("+919652055338", ms)