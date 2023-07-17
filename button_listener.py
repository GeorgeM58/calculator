import tkinter as tk

class ButtonListener:
    def __init__(self, entry):
        self.entry = entry

    def button_click(self, value):
        if value == "=":
            self.calculate()
        elif value == "C":
            self.clear()
        elif value == "sqrt":
            self.entry.insert(tk.END, "math.sqrt(")
        elif value == "mod":
            self.entry.insert(tk.END, "%")
        elif value == "exponent":
            self.entry.insert(tk.END, "**")
        else:
            self.entry.insert(tk.END, str(value))

    def clear(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")