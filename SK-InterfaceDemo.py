# Demonstration of Python GUI elements
# Copyright (C) 2026 Stephen Kent
import tkinter as tk

windowTitle = "SK IntefaceDemo Ver 0.4 by Stephen Kent"
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

# Create the Dice Roller frame
diceFrame = tk.Frame(root, width=500, height=400)
diceFrame.pack(padx=10, pady=10, fill="both", expand=True)

# Create page labels
label1 = tk.Label(frame, text="SK InterfaceDemo", font=("Arial", 24))
label2 = tk.Label(frame, text="by Stephen Kent", font=("Arial", 16))
label1.pack(fill="both", expand=True, pady=2)
label2.pack(fill="both", expand=True, pady=1)

# Helper label with default message
helpLabel = tk.Label(frame, text="Please click a button.")
helpLabel.pack(padx=5, pady=5)

# Button Frame widget for main menu
buttonFrame = tk.Frame(frame, width=490, height=390, background="#cce6ff")
buttonFrame.pack(padx=10, pady=10, fill="both", expand=True)

# Button Frame widget for Dice Roller
buttonFrame2 = tk.Frame(diceFrame, width=490, height=390, background="#cce6ff")
buttonFrame2.pack(padx=10, pady=10, fill="both", expand=True)

# Define button functions
# Display message on button click
def on_click():
    helpLabel.config(text="Under construction, please come back later.")

# Change to Dice Roller frame
def change_to_main():
    frame.pack(padx=10, pady=10, fill="both", expand=True)
    diceFrame.pack_forget()

# Change to Dice Roller frame
def change_to_dice():
    diceFrame.pack(padx=10, pady=10, fill="both", expand=True)
    frame.pack_forget()

# Display buttons
# Button to switch to Dice Roller
diceButton = tk.Button(
    buttonFrame,
    text="Dice Roller",
    command=change_to_dice,
    bg="blue",
    fg="white",
    font=("Arial", 12)
)
diceButton.pack(padx=5, pady=5, side=tk.LEFT)

# Button to switch to Mad Libs
madlibButton = tk.Button(
    buttonFrame,
    text="Mad Libs",
    command=on_click,
    bg="green",
    fg="white",
    font=("Arial", 12)
)
madlibButton.pack(padx=5, pady=5, side=tk.RIGHT)

# Button to return to main menu from Dice Roller
backButton1 = tk.Button(
    buttonFrame2,
    text="Back to main",
    command=change_to_main,
    bg="darkgrey",
    fg="white",
    font=("Arial", 12)
)

# Display an image
image = tk.PhotoImage(file="TestImage01.png")
tk.Label(frame, image=image).pack()

# Generate contents of Dice Roller Frame
# Dice Roller labels
diceLabel1 = tk.Label(diceFrame, text="Dice Roller", font=("Arial", 24))
diceLabel2 = tk.Label(diceFrame, text="Under construction, please come back later.", font=("Arial", 16))
diceLabel1.pack(fill="both", expand=True, pady=2)
diceLabel2.pack(fill="both", expand=True, pady=1)

# Back to main menu button
backButton1.pack(padx=5, pady=5, side=tk.LEFT)

# Display image in Dice Roller
tk.Label(diceFrame, image=image).pack()

# Hide the Dice Roller label on initial load
diceFrame.pack_forget()

# Open window
root.mainloop()