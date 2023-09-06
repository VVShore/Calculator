# import tkinter for root window, text entry input, buttons, and mutable variables
# for gui development
from tkinter import Tk, Entry, Button, StringVar

# defines Calculator class


class Calculator:
    """ 
    Initialize the Calculator application
    Set the initial size and position of the main window
    '357x420' sets the width and height of the window in pixels
    '+0+0' sets the initial position of the window on the screen
    """

    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()  # Create a StringVar to hold the equation
        self.entry_value = ''       # Initializes the entry_value as an empty string
        # Creates entry window where user input appears
        Entry(width=17, bg="#a7d2e8", font=('Helvetica', 28),
              textvariable=self.equation).place(x=0, y=0)

        Button(width=11, height=4, text='(', relief='flat', bg='white',
               command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white',
               command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white',
               command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='white',
               command=lambda: self.show(1)).place(x=0, y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='white',
               command=lambda: self.show(2)).place(x=90, y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='white',
               command=lambda: self.show(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='white',
               command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='white',
               command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='white',
               command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='white',
               command=lambda: self.show(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='white',
               command=lambda: self.show(8)).place(x=180, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='white',
               command=lambda: self.show(9)).place(x=90, y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='white',
               command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='white',
               command=lambda: self.show('.')).place(x=180, y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='white',
               command=lambda: self.show('+')).place(x=270, y=275)
        Button(width=11, height=4, text='-', relief='flat', bg='white',
               command=lambda: self.show('-')).place(x=270, y=200)
        Button(width=11, height=4, text='/', relief='flat', bg='white',
               command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, text='x', relief='flat', bg='white',
               command=lambda: self.show('*')).place(x=270, y=125)
        Button(width=11, height=4, text='=', relief='flat',
               bg='lightblue', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat',
               bg='white', command=self.clear).place(x=0, y=350)

# Method to display a value in the entry field
    def show(self, value):

        # Appends the provided value (as a string) to the current entry_value
        self.entry_value += str(value)

        # Update the text displayed in the Entry widget with the new entry_value
        self.equation.set(self.entry_value)

# Method to clear the entry field
    def clear(self):
        self.entry_value = ''  # Reset the entry_value
        self.equation.set(self.entry_value)  # Clear the text

# Method to calculate and display the result
    def solve(self):

        # Evaluate the mathematical expression stored in entry_value
        result = eval(self.entry_value)

        # Update the text displayed in the Entry widget with the calculated result
        self.equation.set(result)


# Create the main application window
root = Tk()
# Create an instance of the Calculator class, passing the main window as its parent
calculator = Calculator(root)
# Start the Tkinter main event loop to handle user interactions
root.mainloop()
