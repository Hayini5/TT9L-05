import tkinter as tk
from tkinter import messagebox

# Main application window
root = tk.Tk()
root.title('LOGIN')
root.geometry('900x900')

# Load the image
bg_image = tk.PhotoImage(file=r"/Users/vikassni_1304/Downloads/road-highway.png")
root.bg_image = bg_image  # keep a reference to avoid garbage collection

# Background label
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Welcome message
welcome_message = tk.Label(root, text="Welcome to Parking Reservation System of MMU!", font=("Algerian", 36), fg='green', bg=root.cget('bg'))
welcome_message.pack(pady=40)

# Button styles
button_info = {
    "width": 20,
    "height": 2,
    "padx": 10,
    "pady": 10,
    "font": ('Times New Roman', 18)
}

# Function to handle the sign-up process
def button_sign_up():
    # Create a new top-level window for sign up form
    signup_window = tk.Toplevel(root)
    signup_window.title("SIGN UP FORM")

    # Name Label and Entry
    label_name = tk.Label(signup_window, text="Name")
    label_name.grid(row=0, column=0, padx=10, pady=5)

    entry_name = tk.Entry(signup_window)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    # Username Label and Entry
    label_username = tk.Label(signup_window, text="Username")
    label_username.grid(row=1, column=0, padx=10, pady=5)

    entry_username = tk.Entry(signup_window)
    entry_username.grid(row=1, column=1, padx=10, pady=5) 

    # Password Label and Entry
    label_password = tk.Label(signup_window, text="Password")
    label_password.grid(row=2, column=0, padx=10, pady=5)

    entry_password = tk.Entry(signup_window, show="*")
    entry_password.grid(row=2, column=1, padx=10, pady=5)

    # Function to handle submission
    def submit():
        name = entry_name.get()
        username = entry_username.get()
        password = entry_password.get()

        if not name or not username or not password:
            messagebox.showwarning("Input Error", "All fields are required.")
        else:
            # You can add code here to handle the sign-up process (e.g., save details to a database)
            messagebox.showinfo("Sign Up", f"Name: {name}\nUsername: {username}\nPassword: {password}")
            signup_window.destroy()

    # Submit Button
    button_submit = tk.Button(signup_window, text="Submit", command=submit)
    button_submit.grid(row=3, columnspan=2, pady=10)

# GUARD Button
button_guard = tk.Button(root, text="GUARD", **button_info)
button_guard.pack(side="left", padx=150, pady=20)

# STUDENT Button
button_student = tk.Button(root, text="STUDENT", **button_info)
button_student.pack(side="right", padx=150, pady=20)

# SIGN UP Button
button_sign_up_main = tk.Button(root, text="SIGN UP", command=button_sign_up, **button_info)
button_sign_up_main.pack(side="bottom", pady=135)

# Start the Tkinter event loop

root.mainloop()


