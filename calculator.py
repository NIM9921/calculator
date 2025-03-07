from tkinter import Tk, Entry, Button, StringVar
import math  # import math module


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("360x510")
        master.configure(bg='black')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""
        Entry(width=22, bg='#333333', fg='white', font=('Arial Bold', 20), textvariable=self.equation, bd=0, justify='right').place(x=12, y=8)

        # Button styles and layout settings

        left_padding = 5  # padding for button positioning
        button_bg = '#444444'
        button_fg = 'white'
        operator_bg = '#555555'
        special_bg = '#666666'
        button_special = '#ff9500'

        # create buttons for numbers,operations and functions
        # Row 1
        Button(width=7, height=3, text='(', bg=special_bg, fg=button_fg, font=('Arial Bold', 12), command=lambda: self.show('(')).place(x=0 + left_padding, y=50)
        Button(width=7, height=3, text=')', relief='flat', bg=special_bg, fg=button_fg, font=('Arial Bold', 12), command=lambda: self.show(')')).place(x=90 + left_padding, y=50)
        Button(width=7, height=3, text='%', relief='flat', bg=special_bg, fg=button_fg, font=('Arial Bold', 12), command=lambda: self.show('%')).place(x=180 + left_padding, y=50)
        Button(width=7, height=3, text='/', relief='flat', bg=operator_bg, fg=button_fg, font=('Arial Bold', 12), command=lambda: self.show('/')).place(x=270 + left_padding, y=50)

        # Row 2
        Button(width=7, height=3, text='7', relief='flat', bg=button_bg, fg=button_fg, font=('Arial Bold', 12),command=lambda: self.show(7)).place(x=0 + left_padding, y=125)
        Button(width=7, height=3, text='8', relief='flat', bg=button_bg, fg=button_fg, font=('Arial Bold', 12),command=lambda: self.show(8)).place(x=90 + left_padding, y=125)
        Button(width=7, height=3, text='9', relief='flat', bg=button_bg, fg=button_fg, font=('Arial Bold', 12),  command=lambda: self.show(9)).place(x=180 + left_padding, y=125)
        Button(width=7, height=3, text='*', relief='flat', bg=operator_bg, fg=button_fg, font=('Arial Bold', 12), command=lambda: self.show('*')).place(x=270 + left_padding, y=125)

        # Row 3
        Button(width=7, height=3, text='4', relief='flat', bg=button_bg, fg=button_fg, font=('Arial Bold', 12),command=lambda: self.show(4)).place(x=0 + left_padding, y=200)
        Button(width=7, height=3, text='5', relief='flat', bg=button_bg, fg=button_fg, font=('Arial Bold', 12), command=lambda: self.show(5)).place(x=90 + left_padding, y=200)
        Button(width=7, height=3, text='6', relief='flat', bg=button_bg, fg=button_fg, font=('Arial Bold', 12),command=lambda: self.show(6)).place(x=180 + left_padding, y=200)
        Button(width=7, height=3, text='-', relief='flat', bg=operator_bg, fg=button_fg, font=('Arial Bold', 12), command=lambda: self.show('-')).place(x=270 + left_padding, y=200)

        # Row 4
        Button(width=7, height=3, text='1', relief='flat', bg=button_bg, fg=button_fg, font=('Arial Bold', 12), command=lambda: self.show(1)).place(x=0 + left_padding, y=275)
        Button(width=7, height=3, text='2', relief='flat', bg=button_bg, fg=button_fg, font=('Arial Bold', 12), command=lambda: self.show(2)).place(x=90 + left_padding, y=275)
        Button(width=7, height=3, text='3', relief='flat', bg=button_bg, fg=button_fg, font=('Arial Bold', 12),command=lambda: self.show(3)).place(x=180 + left_padding, y=275)
        Button(width=7, height=3, text='+', relief='flat', bg=operator_bg, fg=button_fg, font=('Arial Bold', 12),command=lambda: self.show('+')).place(x=270 + left_padding, y=275)

        # Row 5
        Button(width=7, height=3, text='C', relief='flat', bg=button_special, fg=button_fg, font=('Arial Bold', 12),command=self.clear).place(x=0 + left_padding, y=350)
        Button(width=7, height=3, text='0', relief='flat', bg=button_bg, fg=button_fg, font=('Arial Bold', 12), command=lambda: self.show(0)).place(x=90 + left_padding, y=350)
        Button(width=7, height=3, text='.', relief='flat', bg=special_bg, fg=button_fg, font=('Arial Bold', 12), command=lambda: self.show('.')).place(x=180 + left_padding, y=350)
        Button(width=7, height=3, text='√', relief='flat', bg=operator_bg, fg=button_fg, font=('Arial Bold', 12), command=self.square_root).place(x=270 + left_padding, y=350)

        # Row 6
        Button(width=25, height=3, text='=', relief='flat', bg=operator_bg, fg=button_fg, font=('Arial Bold', 12), command=self.solve).place(x=0 + left_padding, y=425)
        Button(width=7, height=3, text='⌫', relief='flat', bg=operator_bg, fg=button_fg, font=('Arial Bold', 12), command=self.backspace).place(x=270 + left_padding, y=425)

    def show(self, value):

        if self.entry_value != "" and self.entry_value[-1] in ["+", "-", "/", "*", "%", "√"] and str(value) in ["+", "-", "/","*",  "%", "√"]:
            self.entry_value = self.entry_value[:-1] + str(value)
            self.equation.set(self.entry_value)
        else:
            self.entry_value += str(value)
            self.equation.set(self.entry_value)


    def backspace(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception as ex:
            self.equation.set("Error (" + str(ex) + ")")
            self.entry_value = ""

    def square_root(self):
        try:
            result = math.sqrt(float(self.entry_value))
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception as ex:
            self.equation.set("Error (" + str(ex) + ")")
            self.entry_value = ""

# Initialize the Tkinter root window
root = Tk()
calculator = Calculator(root)
root.mainloop()