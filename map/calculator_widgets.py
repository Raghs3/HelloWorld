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
