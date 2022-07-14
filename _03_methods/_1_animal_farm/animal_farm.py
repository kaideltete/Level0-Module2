import sys
import tkinter as tk
from tkinter import simpledialog, Tk
from PIL import Image, ImageTk
from playsound import playsound

window = None


def animals():
    global window
    window = Tk()
    window.withdraw()

    # TODO 1. Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.
    q1 = simpledialog.askstring(title='guess', prompt="which animal do you want want? cat, cow, dog, duck, llama?")
    # TODO 2. Make it so that the user can keep entering new animals.
    while(True):

        q1 = simpledialog.askstring(title='guess', prompt="which animal do you want want? cat, cow, dog, duck, llama?")

    # TODO 3. If the user enters 'exit', stop the program
        if q1=="cat":
            meow()
            sys.exit(0)
        if q1=="cow":
            moo()
            sys.exit(0)
        if q1=="dog":
            woof()
            sys.exit(0)
        if q1=="duck":
            quack()
            sys.exit(0)
        if q1=="llama":
            llama_scream()
            sys.exit(0)
# ======================= DO NOT EDIT THE CODE BELOW =========================

def show_image(filename=None):
    try:
        image = Image.open(filename)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)
        return

    # Put the image on the Tk window used by simpledialog so that when the
    # window with the image is closed, the interpreter moves to the next
    # line of code
    global window
    window.deiconify()
    image = ImageTk.PhotoImage(image)
    tk.Label(master=window, image=image).pack()

    # Blocks so picture can be shown--resumes when picture window is closed
    window.mainloop()

    # Regenerate a new window after closing so more simpledialogs and
    # images can be shown
    window = Tk()
    window.withdraw()


def moo():
    show_image('cow.jpg')
    playsound('moo.wav')


def quack():
    show_image('duck.jpg')
    playsound('quack.wav')


def woof():
    show_image('dog.jpg')
    playsound('woof.wav')


def meow():
    show_image('cat.jpg')
    playsound('meow.wav')


def llama_scream():
    show_image('llama.jpg')
    playsound('llama.wav')


if __name__ == '__main__':
    animals()
