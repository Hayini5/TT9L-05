#from main branch
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('MMU 2')
root.geometry('626x295')

# Load the image
bg_image = tk.PhotoImage(file=r"C:\Users\KARTHIGHAYINI\Downloads\parkinglot.png")

# Keep a reference to the image to prevent garbage collection
root.bg_image = bg_image

# Create a label to display the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
 
# Create a button to trigger the function
button = tk.Button(root, text="GUARD")
button.pack(side="left", padx=110)  # Place the button on the left side with some padding

button = tk.Button(root, text="STUDENT")
button.pack(side="right", padx=110)  # Place the button on the right side with some padding

button = tk.Button(root, text="SIGN UP")
button.pack(side="bottom", padx=10)  # Place the button on the bottom with some padding

button = tk.Button(root, text="SIGN in")
button.pack(side="bottom", padx=10)  # Place the button on the bottom with some padding


root.mainloop() 
