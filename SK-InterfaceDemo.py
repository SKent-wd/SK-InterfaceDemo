#Demonstration of Python GUI elements
#Copyright (C) 2026 Stephen Kent
import tkinter as tk

windowTitle = "SK IntefaceDemo Ver 0.2 by Stephen Kent"
print("Opening " + windowTitle)

#Create main window
root = tk.Tk()

# Set window properties
root.title(windowTitle)
root.configure(background="#004488")
root.minsize(400, 300)
root.maxsize(800, 700)
root.geometry("500x400+50+50")

# Create page labels
label1 = tk.Label(root, text="SK InterfaceDemo", font=("Arial", 25))
label2 = tk.Label(root, text="by Stephen Kent", font=("Arial", 20))
label1.pack()
label2.pack()

#Helper label
helpLabel = tk.Label(root, text="Please click a button.")
helpLabel.pack(padx=5, pady=5)

#Define button functions
def on_click():
    helpLabel.config(text="Under construction, please come back later.")

#Display buttons
diceButton = tk.Button(
    root,
    text="Dice roller",
    command=on_click,
    bg="blue",
    fg="white",
    font=("Arial", 12)
)
diceButton.pack(padx=5, pady=5)

madlibButton = tk.Button(
    root,
    text="Mad libs",
    command=on_click,
    bg="green",
    fg="white",
    font=("Arial", 12)
)
madlibButton.pack(padx=5, pady=5)

# Display an image
image = tk.PhotoImage(file="TestImage01.png")
tk.Label(root, image=image).pack()

#Open window
root.mainloop()