import tkinter as tk

def button_click(event):
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("Калькулятор")


entry = tk.Entry(root, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Helvetica", 20), padx=20, pady=20)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", button_click)

root.mainloop()
