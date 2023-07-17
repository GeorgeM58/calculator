import math
import tkinter as tk

class CalculatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Graphing Calculator")

        self.entry = tk.Entry(self.window, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.button_values = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '(', ')', 'sin', 'cos',
            'tan', '^', 'sqrt',
            'log10', 'ln', 'abs',
            'floor', 'ceil', 'pi', 'e',
            'C'
        ]

        row, col = 1, 0
        self.buttons = []
        for value in self.button_values:
            btn = tk.Button(self.window, text=value, width=5, font=('Arial', 12))
            btn.grid(row=row, column=col, padx=5, pady=5)
            btn.bind("<Button-1>", self.button_click)  # Bind left mouse click event
            self.buttons.append(btn)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.window.bind("<Key>", self.keyboard_input)  # Bind keyboard input event

    def run(self):
        self.window.mainloop()

    def button_click(self, event):
        value = event.widget.cget("text")
        if value == "=":
            self.calculate()
        elif value == "C":
            self.clear()
        else:
            # Append the value to the existing expression
            self.entry.insert(tk.END, value)

    def keyboard_input(self, event):
        value = event.char
        if value.isdigit() or value in ['+', '-', '*', '/', '.', '(', ')']:
            self.entry.insert(tk.END, value)
        elif value == "=" or event.keysym == "Return":
            self.calculate()
        elif value.lower() == "c" or event.keysym == "BackSpace":
            self.clear()

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def clear(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    calc = CalculatorGUI()
    calc.run()