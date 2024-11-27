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

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')  # , fill=tkinter.BOTH, expand=True)  # using X instead of Y doesn't work, have to use extra parameter, works if side is top, but then Y doesn't work
# X for horizontal, Y for vertical
rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)  # pack only for very simple layouts
button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")
button1.pack(side='top')  # , anchor='n')
button2.pack(side='top')  # , anchor='s')  # when widgets share same side, placed adjacent to each other, if no anchor used
button3.pack(side='top')  # , anchor='e')  # anchor affects widget based on which edge side is packed, east & west for top, north & south for left

mainWindow.mainloop()
