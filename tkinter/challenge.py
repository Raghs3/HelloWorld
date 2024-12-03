# import tkinter
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("Calculator")
# mainWindow['padx'] = 8
#
# # Result
# result = tkinter.Entry(mainWindow)
# result.grid(row=0, column=0, columnspan=4, sticky='w')
#
# # Clear Buttons
# cButton = tkinter.Button(mainWindow, text="C")
# cButton.grid(row=1, column=0, sticky='news')
#
# ceButton = tkinter.Button(mainWindow, text="CE")
# ceButton.grid(row=1, column=1, sticky='news')
#
# # numbers
# # for i in range(9, -1, -1):
# #     numButton = tkinter.Button(mainWindow, text=i)
# #     for j in range(0, 4):
# #         for k in range(0, 4):
# #             numButton.grid(row=2+j, column=0+k, sticky='news')
#
# num0Button = tkinter.Button(mainWindow, text="0")
# num1Button = tkinter.Button(mainWindow, text="1")
# num2Button = tkinter.Button(mainWindow, text="2")
# num3Button = tkinter.Button(mainWindow, text="3")
# num4Button = tkinter.Button(mainWindow, text="4")
# num5Button = tkinter.Button(mainWindow, text="5")
# num6Button = tkinter.Button(mainWindow, text="6")
# num7Button = tkinter.Button(mainWindow, text="7")
# num8Button = tkinter.Button(mainWindow, text="8")
# num9Button = tkinter.Button(mainWindow, text="9")
#
# num7Button.grid(row=2, column=0, sticky='news')
# num8Button.grid(row=2, column=1, sticky='news')
# num9Button.grid(row=2, column=2, sticky='news')
# num4Button.grid(row=3, column=0, sticky='news')
# num5Button.grid(row=3, column=1, sticky='news')
# num6Button.grid(row=3, column=2, sticky='news')
# num1Button.grid(row=4, column=0, sticky='news')
# num2Button.grid(row=4, column=1, sticky='news')
# num3Button.grid(row=4, column=2, sticky='news')
# num0Button.grid(row=5, column=0, sticky='news')
#
# # symbols
#
# addButton = tkinter.Button(mainWindow, text="+")
# subButton = tkinter.Button(mainWindow, text="-")
# multButton = tkinter.Button(mainWindow, text="*")
# divButton = tkinter.Button(mainWindow, text="/")
# equalButton = tkinter.Button(mainWindow, text="=")
#
# addButton.grid(row=2, column=3, sticky='nsew')
# subButton.grid(row=3, column=3, sticky='nsew')
# multButton.grid(row=4, column=3, sticky='nsew')
# divButton.grid(row=5, column=3, sticky='nsew')
# equalButton.grid(row=5, column=1, columnspan=2, sticky='nsew')
#
# mainWindow.mainloop()


# TIM SOLN

import tkinter

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 2),('/', 1)],
        ]

mainWindowPadding = 8

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

row = 1
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + 50 + mainWindowPadding, result.winfo_height() + 50 + keyPad.winfo_height())

mainWindow.mainloop()
