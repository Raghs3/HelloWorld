import sqlite3
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

conn = sqlite3.connect('music.db')

mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browser")
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)  # spacer column on right

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)
