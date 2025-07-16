import tkinter as tk
import tkinter.messagebox


class CalculatorButton(tk.Button):
    """A button with callback, to be used with a CalculatorGrid widget"""

    def __init__(self, master, callback=None, **kwargs):
        # self.callback = kwargs.pop('callback', None)
        self.callback = callback
        super().__init__(master, **kwargs)
        self.config(command=self.on_click)

    def on_click(self):
        if self.callback:
            self.callback(self['text'])


def test():
    def clicked(caption: str):
        print(f'{caption} was clicked')

    main_window = tk.Tk()
    main_window.title("CalculatorButton test")
    main_window.geometry('640x480')

    btn = CalculatorButton(main_window, callback=clicked, text='Test')
    btn.grid(row=0, column=0, sticky='nsew')

    main_window.mainloop()


if __name__ == '__main__'
    test()
