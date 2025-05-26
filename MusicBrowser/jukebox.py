import sqlite3
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

conn = sqlite3.connect('music.db')
