import tkinter as tk
from tkinter import messagebox

# Main application window
root = tk.Tk()
root.title('LOGIN')
root.geometry('900x900')

# Load the image
bg_image = tk.PhotoImage(file=r"C:\Users\R. Prashanthy Pathy\Pictures\road-highway.png")
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
    signup_window.geometry('900x900')

    signup_bg_image = tk.PhotoImage(file=r"C:\Users\R. Prashanthy Pathy\Pictures\signup.png")
    signup_window.bg_image = signup_bg_image
    signup_bg_label = tk.Label(signup_window, image=signup_bg_image)
    signup_bg_label.place(relwidth=1, relheight=1)

    signupform_frame = tk.Frame(signup_window, bg='black', bd=10)
    signupform_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Name Label and Entry
    label_name = tk.Label(signupform_frame, text="Name", bg='black', fg='white')
    label_name.grid(row=0, column=0, padx=10, pady=5)

    entry_name = tk.Entry(signupform_frame)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    # Username Label and Entry
    label_username = tk.Label(signupform_frame, text="Username", bg='black', fg='white')
    label_username.grid(row=1, column=0, padx=10, pady=5)

    entry_username = tk.Entry(signupform_frame)
    entry_username.grid(row=1, column=1, padx=10, pady=5)

    # Password Label and Entry
    label_password = tk.Label(signupform_frame, text="Password", bg='black', fg='white')
    label_password.grid(row=2, column=0, padx=10, pady=5)

    entry_password = tk.Entry(signupform_frame, show="*")
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
    button_submit = tk.Button(signupform_frame, text="SIGN UP", command=submit)
    button_submit.grid(row=3, columnspan=2, pady=10)

# Function to handle the guard login process
def button_guard():
    # Create a new top-level window for guard login form
    guard_login_window = tk.Toplevel(root)
    guard_login_window.title("GUARD LOGIN")

    # Guard_Id Label and Entry
    label_guard_id = tk.Label(guard_login_window, text="Guard_Id")
    label_guard_id.grid(row=0, column=0, padx=10, pady=5)

    entry_guard_id = tk.Entry(guard_login_window)
    entry_guard_id.grid(row=0, column=1, padx=10, pady=5)

    # Password Label and Entry
    label_password = tk.Label(guard_login_window, text="Password")
    label_password.grid(row=1, column=0, padx=10, pady=5)

    entry_password = tk.Entry(guard_login_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    # Function to handle login submission
    def login():
        guard_id = entry_guard_id.get()
        password = entry_password.get()

        if not guard_id or not password:
            messagebox.showwarning("Input Error", "Both fields are required.")
        else:
            # Add code here to handle the login process (e.g., verify credentials)
            messagebox.showinfo("Login", f"guard_id: {guard_id}\nPassword: {password}")
            guard_login_window.destroy()
            open_faculty_selection()

    # Login Button
    button_login = tk.Button(guard_login_window, text="Login", command=login)
    button_login.grid(row=2, columnspan=2, pady=10)

# Function to open the faculty selection window
def open_faculty_selection():
    faculty_window = tk.Toplevel(root)
    faculty_window.title("Faculty Selection")

    label = tk.Label(faculty_window, text="Which faculty?", font=("Times New Roman", 24))
    label.pack(pady=20)

    # Example buttons for different faculties
    button_faculty1 = tk.Button(faculty_window, text="FCI", font=("Times New Roman", 18))
    button_faculty1.pack(pady=10)

    button_faculty2 = tk.Button(faculty_window, text="FOE", font=("Times New Roman", 18))
    button_faculty2.pack(pady=10)


# GUARD Button
button_guard_main = tk.Button(root, text="GUARD", command=button_guard, **button_info)
button_guard_main.pack(side="left", padx=150, pady=20)

# STUDENT Button
button_student = tk.Button(root, text="STUDENT", **button_info)
button_student.pack(side="right", padx=150, pady=20)

# SIGN UP Button
button_sign_up_main = tk.Button(root, text="SIGN UP", command=button_sign_up, **button_info)
button_sign_up_main.pack(side="bottom", pady=135)

# Start the Tkinter event loop
root.mainloop()
