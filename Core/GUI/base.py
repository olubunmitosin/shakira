from tkinter import *

import pyttsx3
from gtts import gTTS

from Engines.text_to_speech import configure_engine

root = Tk()
message_field: Entry()

# Configure voice engine
engine = configure_engine()


def draw_window(message: StringVar, clear_string) -> Tk:
    global message_field

    root.geometry("550x300")
    root.configure(bg='ghost white')
    root.title("Shakira")
    Label(root, text="Text to speech", font="arial 20 bold", bg="white smoke").pack()
    Label(root, text="Shakira", font="arial 15 bold", bg="white smoke", width="20").pack(side="bottom")
    Label(root, text="Type your text", font="arial 15 bold", bg="white smoke").place(x=20, y=60)
    entry_field = message_field = Entry(root, textvariable=message, width="50")
    entry_field.place(x=20, y=100)
    Button(root, text="Play", font="arial 15 bold", width="4", command=run_action).place(x=25, y=140)
    Button(root, text="Exit", font="arial 15 bold", width="4", command=close_window, bg="OrangeRed1").place(x=100,
                                                                                                            y=140)
    Button(root, text="Clear field", font="arial 15 bold", command=clear_string, width="6").place(x=175, y=140)
    return root


def close_window():
    root.destroy()


def run_action():
    message = message_field.get()
    engine.say(text=message)
    engine.runAndWait()
    root.update()
