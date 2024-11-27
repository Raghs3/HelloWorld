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
canvas.pack(side='left')  # , fill=tkinter.BOTH, expand=True)  # using X instead of Y doesn't work, have to use extra parameter, works if side is top, but then Y doesnt work
# X for horizontal, Y for vertical
button1 = tkinter.Button(mainWindow, text="Button1")
button2 = tkinter.Button(mainWindow, text="Button2")
button3 = tkinter.Button(mainWindow, text="Button3")
button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')  # when widgets share same side, placed adjacent to each other

mainWindow.mainloop()
