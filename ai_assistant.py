from logging import root
import wikipedia
import webbrowser
import facerec as f
import cam2 as c2
import methods as m
import pywhatkit
import numpy as np
import pyautogui
import tkinter as tk
from tkinter import Label, Button, Text
import speech_recognition as sr
import pyttsx3
import datetime
import tkinter as tk



def execute_command():
    m.speak("welcome home sir")
    while True:
        my_text = m.commands()
        if my_text == None:
            continue
        if 'date' in my_text:
            m.date()
        elif 'search' in my_text:
            my_text = my_text.replace("search", "")
            pywhatkit.search(my_text)
        elif 'google' in my_text:
            my_text = my_text.replace("google", "")
            pywhatkit.search(my_text)
        elif 'open youtube' in my_text:
            m.speak("Opening YouTube")
            webbrowser.open("youtube.com")
        elif 'open maps' in my_text:
            m.speak("Opening maps")
            webbrowser.open("google.com/maps")
        elif 'open chat gpt' in my_text:
            m.speak("Opening chatGPT")
            webbrowser.open("chatgpt.com")
        elif 'open insta' in my_text:
            m.speak("Opening Instagram")
            webbrowser.open("instagram.com")
        elif 'open amazon prime' in my_text:
            m.speak("Opening AmazonPrime")
            webbrowser.open("primevideo.com")
        elif 'time' in my_text:
            m.time()
        elif 'sir' in my_text:
            m.speak("Sir is a respectful term used to address a man, especially one who is in a position of authority. For me, it is Srujan sir")
        elif 'boss' in my_text:
            m.speak("A boss is an authority figure, often the person who tells you what to do at work. For me, gowtham sir is my boss")
        elif 'play' in my_text:
            my_text = my_text.replace("play", "")
            m.speak('playing ' + my_text)
            pywhatkit.playonyt(my_text)
        elif 'listening' in my_text:
            m.speak("yes sir I am")
        elif "tell me about" in my_text:
            my_text = my_text.replace("tell me about ", "")
            infov = wikipedia.summary(my_text)
            print(infov)
            m.speak(infov)
        elif "send" in my_text:
            m.speak("say your message")
            ms = m.commands()
            try:
                if 'gowtham' in my_text:
                    m.msgme(ms)
                elif 'meghana' in my_text:
                    m.msgmg(ms)
                elif 'mahesh' in my_text:
                    m.msgmh(ms)
                elif 'srujan' in my_text:
                    m.msgsj(ms)
                elif 'sai' in my_text:
                    m.msgsk(ms)
                else:
                    m.msgna(ms)
            except:
                m.speak("no text found")
        elif 'screenshot' in my_text:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            print(f"Screenshot saved as screenshot.png")
        elif 'open camera' in my_text:
            m.speak("opening camera sir")
            f.met()
        elif 'change cam' in my_text or 'change camera' in my_text:
            c2.met()
        elif 'sound' in my_text or 'volume' in my_text:
            m.volume(my_text)
        elif 'exit' in my_text or 'close' in my_text or 'end' in my_text:
            m.speak("Goodbye!")
            root.quit()
            break
        else:
            m.speak("speak again")
        
# Function to display text in the GUI
def display_text(text):
    output_text.insert(tk.END, text + "\n")
    output_text.see(tk.END)

# Tkinter GUI setup
root = tk.Tk()
root.title("Virtual Assistant")

# GUI styling
root.geometry("600x400")  # Window size
root.config(bg="#1e1e1e")  # Background color (dark mode)

# GUI layout
greeting_label = Label(root, text="Virtual Assistant", font=("Helvetica", 18, "bold"), fg="#ffffff", bg="#1e1e1e")
greeting_label.pack(pady=10)

start_button = Button(root, text="Start Assistant", command=execute_command, font=("Helvetica", 12),bg="#4CAF50", fg="white", activebackground="#45a049", width=20, height=2, bd=0)
start_button.pack(pady=20)
output_text = Text(root, height=10, width=60, font=("Courier", 12), fg="#f8f8f2", bg="#2e2e2e", bd=0)
output_text.pack(padx=10, pady=10)
exit_button = Button(root, text="Exit", command=root.quit,font=("Helvetica", 12),bg="#f44336", fg="white", activebackground="#e53935", width=20, height=2, bd=0)
exit_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
