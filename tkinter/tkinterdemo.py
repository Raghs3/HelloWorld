try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter
# tkinter._test()
mainWindow = tkinter.Tk()  # route window

mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='left')

mainWindow.mainloop()
