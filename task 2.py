import tkinter as tk

def button_click(number):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, str(current) + str(number))

def clear():
    entry_display.delete(0, tk.END)

def calculate():
    expression = entry_display.get()
    try:
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")

window = tk.Tk()
window.title("Better Calculator")

entry_display = tk.Entry(window, width=20, font=('Arial', 14), justify='right')
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('4', 2, 0),
    ('5', 2, 1), ('6', 2, 2), ('1', 3, 0), ('2', 3, 1),
    ('3', 3, 2), ('0', 4, 1)
]

for (text, row, column) in buttons:
    button = tk.Button(window, text=text, width=5, height=2, command=lambda t=text: button_click(t))
    button.grid(row=row, column=column, padx=5, pady=5)

operations = ['+', '-', '*', '/']
for i, op in enumerate(operations):
    button = tk.Button(window, text=op, width=5, height=2, command=lambda t=op: button_click(t))
    button.grid(row=i+1, column=3, padx=5, pady=5)

equal_button = tk.Button(window, text='=', width=5, height=2, command=calculate)
equal_button.grid(row=4, column=2, padx=5, pady=5)

clear_button = tk.Button(window, text='C', width=5, height=2, command=clear)
clear_button.grid(row=4, column=0, padx=5, pady=5)

window.mainloop()
