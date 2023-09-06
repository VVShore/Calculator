# import tkinter for gui

from tkinter import Tk, Entry, Button, StringVar

# defines Calculator class


class Calculator:
    # initialize attributes
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg="#fff", font=('Courier New', 28),
              textvariable=self.equation).place(x=0, y=0)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)
        self.equation.set(self)


root = Tk()
calculator = Calculator(root)
root.mainloop()
