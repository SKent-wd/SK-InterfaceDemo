# Demonstration of Python GUI elements
# Copyright (C) 2026 Stephen Kent
import tkinter as tk

windowTitle = "SK IntefaceDemo Ver 0.3 by Stephen Kent"
print("Opening " + windowTitle)

# Create main window
root = tk.Tk()

# Set window properties
root.title(windowTitle)
root.configure(background="#004488")
root.minsize(400, 300)
root.maxsize(800, 700)
root.geometry("500x400+50+50")

# Create main Frame widget
frame = tk.Frame(root, width=500, height=400)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Create page labels
label1 = tk.Label(frame, text="SK InterfaceDemo", font=("Arial", 24))
label2 = tk.Label(frame, text="by Stephen Kent", font=("Arial", 16))
label1.pack(fill="both", expand=True, pady=2)
label2.pack(fill="both", expand=True, pady=1)

# Helper label
helpLabel = tk.Label(frame, text="Please click a button.")
helpLabel.pack(padx=5, pady=5)

# Button Frame widget
buttonFrame = tk.Frame(frame, width=490, height=390, background="#cce6ff")
buttonFrame.pack(padx=10, pady=10, fill="both", expand=True)

# Define button functions
def on_click():
    helpLabel.config(text="Under construction, please come back later.")

# Display buttons
diceButton = tk.Button(
    buttonFrame,
    text="Dice roller",
    command=on_click,
    bg="blue",
    fg="white",
    font=("Arial", 12)
)
diceButton.pack(padx=5, pady=5, side=tk.LEFT)

madlibButton = tk.Button(
    buttonFrame,
    text="Mad libs",
    command=on_click,
    bg="green",
    fg="white",
    font=("Arial", 12)
)
madlibButton.pack(padx=5, pady=5, side=tk.RIGHT)

# Display an image
image = tk.PhotoImage(file="TestImage01.png")
tk.Label(frame, image=image).pack()

# Open window
root.mainloop()