import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('LOGIN')
root.geometry(f'1195x733')

bg_image = tk.PhotoImage(file=r"/Users/vikassni_1304/Downloads/parking pic.png")

root.bg_image = bg_image

bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

button_info = {
    "width": 20,
    "height": 2,
    "padx": 10,
    "pady": 10,
    "font": ('Times New Roman', 16)
}
 
button = tk.Button(root, text="GUARD", **button_info)
button.pack(side="left", padx=150, pady=20)  

button = tk.Button(root, text="STUDENT", **button_info)
button.pack(side="right", padx=150, pady=20)  

button = tk.Button(root, text="SIGN UP", **button_info)
button.pack(side="bottom", pady=135)  

root.mainloop() 
