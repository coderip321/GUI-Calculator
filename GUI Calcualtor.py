import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")

        # Entry widget for displaying input and results
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.entry_var, font=('Arial', 14), bd=10, insertwidth=4, width=14, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, button_text):
        current_text = self.entry_var.get()

        if button_text == '=':
            try:
                result = str(eval(current_text))
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set('Error')
        else:
            self.entry_var.set(current_text + button_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
