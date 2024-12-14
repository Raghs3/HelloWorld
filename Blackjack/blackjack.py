import random

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

# Set up the screen and frames for the dealer and player
mainWindow.title("Blackjack")
mainWindow.geometry("640x480")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background='green')
