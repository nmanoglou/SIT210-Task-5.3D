
from tkinter import *
import RPi.GPIO as GPIO
from time import *

# setup
GPIO.setmode(GPIO.BCM)

Led = 10

GPIO.setup(Led, GPIO.OUT)
GPIO.output(Led, GPIO.OUT)

# GUI definitions
win = Tk()
win.title("Morse code GUI")

# event function

def short():
    GPIO.output(Led, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(Led, GPIO.LOW)
    sleep(0.5)

def longer():
    GPIO.output(Led, GPIO.HIGH)
    sleep(1)
    GPIO.output(Led, GPIO.LOW)
    sleep(0.5)

def a():
    short()
    longer()

def b():
    longer()
    short()
    short()
    short()

def c():
    longer()
    short()
    longer()
    short()

def d():
    longer()
    short()
    short()

def e():
    short()

def f():
    short()
    short()
    longer()
    short()

def g():
    longer()
    longer()
    short()

def h():
    short()
    short()
    short()
    short()

def i():
    short()
    short()

def j():
    short()
    longer()
    longer()
    longer()

def k():
    longer()
    short()
    longer()

def l():
    short()
    longer()
    short()
    short()

def m():
    longer()
    longer()

def n():
    longer()
    short()

def o():
    longer()
    longer()
    longer()

def p():
    short()
    longer()
    longer()
    short()

def q():
    longer()
    longer()
    short()
    longer()

def r():
    short()
    longer()
    short()

def s():
    short()
    short()
    short()

def t():
    longer()

def u():
    short()
    short()
    longer()

def v():
    short()
    short()
    short()
    longer()

def w():
    short()
    longer()
    longer()

def x():
    longer()
    short()
    short()
    longer()

def y():
    longer()
    short()
    longer()
    longer()

def z():
    longer()
    longer()
    short()
    short()

def close():
    win.destroy()
    GPIO.cleanup

def activateMorse():
    word = entryBox.get()
    word = word.Lower()
    counter = 0

    while counter < 12:
        for letter in word:
            if letter == "a":
                a()
                counter += 1
                continue
            elif letter == "b":
                b()
                counter += 1
                continue
            elif letter == "c":
                c()
                counter += 1
                continue
            elif letter == "d":
                d()
                counter += 1
                continue
            elif letter == "e":
                e()
                counter += 1
                continue
            elif letter == "f":
                f()
                counter += 1
                continue
            elif letter == "g":
                g()
                counter += 1
                continue
            elif letter == "h":
                h()
                counter += 1
                continue
            elif letter == "i":
                i()
                counter += 1
                continue
            elif letter == "j":
                j()
                counter += 1
                continue
            elif letter == "k":
                k()
                counter += 1
                continue
            elif letter == "l":
                l()
                counter += 1
                continue
            elif letter == "m":
                m()
                counter += 1
                continue
            elif letter == "n":
                n()
                counter += 1
                continue
            elif letter == "o":
                o()
                counter += 1
                continue
            elif letter == "p":
                p()
                counter += 1
                continue
            elif letter == "q":
                q()
                counter += 1
                continue
            elif letter == "r":
                r()
                counter += 1
                continue
            elif letter == "s":
                s()
                counter += 1
                continue
            elif letter == "t":
                t()
                counter += 1
                continue
            elif letter == "u":
                u()
                counter += 1
                continue
            elif letter == "v":
                v()
                counter += 1
                continue
            elif letter == "w":
                w()
                counter += 1
                continue
            elif letter == "x":
                x()
                counter += 1
                continue
            elif letter == "y":
                y()
                counter += 1
                continue
            elif letter == "z":
                z()
                counter += 1
                continue




# widgets
entryBoxLabel = Label(win, Text = 'Enter a name to display in morse code (12 characters max)')
entryBoxLabel.grid(row = 0, column = 0)

entryBox = Entry(win)
entryBox.grid(row = 2, column = 0)

submitButton = Button(win, text = "Submit", command = activateMorse)
submitButton.grid(row = 4, column = 0)

exitButton = Button(win, text = "Exit", command = close)
exitButton.grid(row = 6, clumn = 0)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()