try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter
# tkinter._test()
mainWindow = tkinter.Tk()  # route window

mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+200')

label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)  # row, column for grid

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)  # , fill=tkinter.BOTH, expand=True)  # using X instead of Y doesn't work, have to use extra parameter, works if side is top, but then Y doesn't work
# X for horizontal, Y for vertical
rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')  # pack only for very simple layouts
button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")
button1.grid(row=0, column=0)  # , anchor='n')
button2.grid(row=1, column=0)  # , anchor='s')  # when widgets share same side, placed adjacent to each other, if no anchor used
button3.grid(row=2, column=0)  # , anchor='e')  # anchor affects widget based on which edge side is packed, east & west for top, north & south for left

# configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)  # both are the same, grid_columnconfigure calls columnconfigure

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)  # doing this, button 2 expands to fill the entire space
button2.grid(sticky='ew')  # unless weight specified sticky might not do anything

mainWindow.mainloop()
