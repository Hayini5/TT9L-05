<<<<<<< HEAD
=======
#from main to karthighayini
>>>>>>> main
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('LOGIN')
<<<<<<< HEAD
<<<<<<< HEAD
root.geometry(f'1195x733')
=======
root.geometry('625x295')
>>>>>>> main

bg_image = tk.PhotoImage(file=r"/Users/vikassni_1304/Downloads/parking pic.png")
=======
root.geometry('900x900')

# Load the image
bg_image = tk.PhotoImage(file=r"C:\Users\KARTHIGHAYINI\Downloads\PARKING PIC.png")
>>>>>>> c75c067df5651fa7b8340069ede46908a650c57a

root.bg_image = bg_image

bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

welcome_message = tk.Label(root, text="Welcome to Parking Reservation System!", font=("Arial", 28))
welcome_message.pack(pady=20)


button_info = {
    "width": 20,
    "height": 2,
    "padx": 10,
    "pady": 10,
    "font": ('Times New Roman', 16)
}
 
<<<<<<< HEAD
def button_sign_up():
    name = tk.Label("Sign Up", "Enter your name:")
    username = tk.Label("Sign Up", "Enter your username:")
    password = tk.Label("Sign Up", "Enter your password:")
                            
button_guard = tk.Button(root, text="GUARD", **button_info)
button_guard.pack(side="left", padx=150, pady=20)  

button_student = tk.Button(root, text="STUDENT", **button_info)
button_student.pack(side="right", padx=150, pady=20)  

button_sign_up = tk.Button(root, text="SIGN UP", **button_info)
button_sign_up.pack(side="bottom", pady=135)  

=======
# Create a button to trigger the function
button = tk.Button(root, text="GUARD")
button.pack(side="left", padx=250)  # Place the button on the left side with some padding

button = tk.Button(root, text="STUDENT")
button.pack(side="right", padx=250)  # Place the button on the right side with some padding

button = tk.Button(root, text="SIGN UP")
button.pack(side="bottom", padx=10)  # Place the button on the bottom with some padding
>>>>>>> c75c067df5651fa7b8340069ede46908a650c57a

root.mainloop() 
