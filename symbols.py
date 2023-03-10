import tkinter as tk

def count_symbols(*args):
    text = input_var.get()   # Get the current input string
    num_symbols = len(text)  # Calculate the number of symbols in the string
    label_var.set(f"Number of symbols: {num_symbols}")  # Update the label text

root = tk.Tk()


# Create an input field with a StringVar
input_var = tk.StringVar() 
input_var.trace("w", count_symbols)
input_entry = tk.Entry(root, textvariable=input_var,border=10, width=50, bg="blue", fg="white")
input_entry.pack()

# Create a label to display the number of symbols
label_var = tk.StringVar()
label_var.set("Number of symbols: 0")
label = tk.Entry(root, textvariable=label_var, border=10, width=50, bg="yellow", fg="black")
label.pack()
root.mainloop()