import tkinter as tk

def button_click(value):
    if value == "Enter":
        # Handle the Enter button click
        current_text = entry.get()
        # You can perform some action with the input here
        entered_label.config(text=f"Entered: {current_text}")
        entry.delete(0, tk.END)  # Clear the entry field
    elif value == "Back":
        # Handle the Backspace button click
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text[:-1])
    else:
        # Handle number button click
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text + value)

# Create the main window
root = tk.Tk()
root.title("Numpad")

# Create an Entry widget for displaying the input
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, columnspan=3)

# Create a label to show the entered number
entered_label = tk.Label(root, text="", font=("Arial", 16))
entered_label.grid(row=1, column=0, columnspan=3)

# Create the numpad buttons
buttons = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0", "Back", "Enter"
]

row, col = 2, 0

for button in buttons:
    tk.Button(root, text=button, width=15, height=6, command=lambda b=button: button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1

root.geometry("345x439")
root.mainloop()
