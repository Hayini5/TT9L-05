import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('parking_system.db')

# Create a cursor object
c = conn.cursor()

# Create a table for users
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        user_id TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

# Main application window
root = tk.Tk()
root.title('LOGIN')
root.geometry('900x900')

# Load the image
bg_image = tk.PhotoImage(file=r"C:\Users\KARTHIGHAYINI\Downloads\road-highway.png")
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

def button_sign_up():
    # Create a new top-level window for sign up form
    signup_window = tk.Toplevel(root)
    signup_window.title("SIGN UP SELECTION")
    signup_window.geometry('900x900')

    signup_bg_image = tk.PhotoImage(file=r"C:\Users\KARTHIGHAYINI\Downloads\WhatsApp-Image-2024-06-05-at-2.07.03-AM.png")
    signup_window.bg_image = signup_bg_image
    signup_bg_label = tk.Label(signup_window, image=signup_bg_image)
    signup_bg_label.place(relwidth=1, relheight=1)

    signupselection_frame = tk.Frame(signup_window, bg='black', bd=10)
    signupselection_frame.place(relx=0.5, rely=0.4, anchor='center')  # Adjust the rely parameter to move the frame up

    # Label and Entry
    label = tk.Label(signupselection_frame, text="ARE YOU A STUDENT OR A GUARD TO SIGN UP?", fg='black', bg='white',font=("Times New Roman", 16))
    label.grid(row=0,column=0,padx=10,pady=5)

    # Create a new frame for the buttons
    button_frame = tk.Frame(signup_window, bg='black', bd=10)
    button_frame.place(relx=0.5, rely=0.6, anchor='center')  # Adjust the rely parameter to move the frame down

    # Example buttons for different users
    button_user1 = tk.Button(button_frame, text="STUDENT", font=("Times New Roman", 18), command=student_sign_up)
    button_user1.grid(row=0, column=0, padx=10, pady=10)

    button_user2 = tk.Button(button_frame, text="GUARD", font=("Times New Roman", 18), command=guard_sign_up)
    button_user2.grid(row=0, column=1, padx=10, pady=10)

def student_sign_up():
    # Create a new top-level window for sign up form
    signup_window = tk.Toplevel(root)
    signup_window.title("SIGN UP FORM")
    signup_window.geometry('900x900')

    signup_bg_image = tk.PhotoImage(file=r"C:\Users\KARTHIGHAYINI\Downloads\WhatsApp-Image-2024-06-05-at-2.07.03-AM.png")
    signup_window.bg_image = signup_bg_image
    signup_bg_label = tk.Label(signup_window, image=signup_bg_image)
    signup_bg_label.place(relwidth=1, relheight=1)

    signupform_frame = tk.Frame(signup_window, bg='black', bd=10)
    signupform_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Name Label and Entry
    label_name = tk.Label(signupform_frame, text="Name", fg='black', bg='white')
    label_name.grid(row=0, column=0, padx=10, pady=5)

    entry_name = tk.Entry(signupform_frame)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    # ID Label and Entry
    label_id = tk.Label(signupform_frame, text="ID", fg='black', bg='white')
    label_id.grid(row=1, column=0, padx=10, pady=5)

    entry_id = tk.Entry(signupform_frame)
    entry_id.grid(row=1, column=1, padx=10, pady=5)

    # Password Label and Entry
    label_password = tk.Label(signupform_frame, text="Password", fg='black', bg='white')
    label_password.grid(row=2, column=0, padx=10, pady=5)

    entry_password = tk.Entry(signupform_frame, show="*")
    entry_password.grid(row=2, column=1, padx=10, pady=5)
    
    def toggle_password():
        if entry_password.cget('show')== '':
            entry_password.config(show='*')
            toggle_button.config(text='show')
        else:
            entry_password.config(show='')
            toggle_button.config(text='hide')
            
        
    toggle_button = tk.Button(signupform_frame, text='Show', command=toggle_password)
    toggle_button.grid(row=2, column=2, padx=10, pady=5)

    # Function to handle submission
    def submit():
        name = entry_name.get()
        user_id = entry_id.get()
        password = entry_password.get()

        if not name or not user_id or not password:
            messagebox.showwarning("Input Error", "All fields are required.")
        else:
            # Insert user data into the SQLite database
            try:
                conn = sqlite3.connect('parking_system.db')
                c = conn.cursor()
                c.execute('''
                    INSERT INTO users (name, user_id, password) VALUES (?, ?, ?)
                ''', (name, user_id, password))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sign Up", "Sign Up Successful!")
                signup_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "User ID already exists. Please choose a different one.")

    # Submit Button
    button_submit = tk.Button(signupform_frame, text="SIGN UP", command=submit)
    button_submit.grid(row=3, columnspan=2, pady=10)

def guard_sign_up():
    # Create a new top-level window for sign up form
    signup_window = tk.Toplevel(root)
    signup_window.title("SIGN UP FORM")
    signup_window.geometry('900x900')

    signup_bg_image = tk.PhotoImage(file=r"C:\Users\KARTHIGHAYINI\Downloads\WhatsApp-Image-2024-06-05-at-2.07.03-AM.png")
    signup_window.bg_image = signup_bg_image
    signup_bg_label = tk.Label(signup_window, image=signup_bg_image)
    signup_bg_label.place(relwidth=1, relheight=1)

    signupform_frame = tk.Frame(signup_window, bg='black', bd=10)
    signupform_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Name Label and Entry
    label_name = tk.Label(signupform_frame, text="Name", fg='black', bg='white')
    label_name.grid(row=0, column=0, padx=10, pady=5)

    entry_name = tk.Entry(signupform_frame)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    # ID Label and Entry
    label_id = tk.Label(signupform_frame, text="ID", fg='black', bg='white')
    label_id.grid(row=1, column=0, padx=10, pady=5)

    entry_id = tk.Entry(signupform_frame)
    entry_id.grid(row=1, column=1, padx=10, pady=5)

    # Password Label and Entry
    label_password = tk.Label(signupform_frame, text="Password", fg='black', bg='white')
    label_password.grid(row=2, column=0, padx=10, pady=5)

    entry_password = tk.Entry(signupform_frame, show="*")
    entry_password.grid(row=2, column=1, padx=10, pady=5)

    
    def toggle_password():
        if entry_password.cget('show')== '':
            entry_password.config(show='*')
            toggle_button.config(text='show')
        else:
            entry_password.config(show='')
            toggle_button.config(text='hide')
            
        
    toggle_button = tk.Button(signupform_frame, text='Show', command=toggle_password)
    toggle_button.grid(row=2, column=2, padx=10, pady=5)

    # Function to handle submission
    def submit():
        name = entry_name.get()
        guard_id = entry_id.get()
        password = entry_password.get()

        if not name or not guard_id or not password:
            messagebox.showwarning("Input Error", "All fields are required.")
        else:
            # Insert user data into the SQLite database
            try:
                conn = sqlite3.connect('parking_system.db')
                c = conn.cursor()
                c.execute('''
                    INSERT INTO users (name, user_id, password) VALUES (?, ?, ?)
                ''', (name, guard_id, password))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sign Up", "Sign Up Successful!")
                signup_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Guard ID already exists. Please choose a different one.")

    # Submit Button
    button_submit = tk.Button(signupform_frame, text="SIGN UP", command=submit)
    button_submit.grid(row=3, columnspan=2, pady=10)

# Function to handle the student login process
def button_student_login():
    # Create a new top-level window for login form
    student_window = tk.Toplevel(root)
    student_window.title('STUDENT LOGIN FORM')
    student_window.geometry('900x900')

    student_bg_image = tk.PhotoImage(file=r"C:\Users\KARTHIGHAYINI\Downloads\WhatsApp-Image-2024-06-05-at-2.07.03-AM.png")
    student_window.bg_image = student_bg_image  # keep a reference to avoid garbage collection
    student_bg_label = tk.Label(student_window, image=student_bg_image)
    student_bg_label.place(relwidth=1, relheight=1)

    # Create a frame to hold the login form
    loginform_frame = tk.Frame(student_window, bg='white', bd=10)
    loginform_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Student heading text
    student_heading = tk.Label(loginform_frame, text="STUDENT LOGIN", font=("Microsoft YaHei UI Light", 23, 'bold'), fg='black', bg='white')
    student_heading.grid(row=0, columnspan=2, pady=20)

    # Student_ID Label and Entry
    label_student_id = tk.Label(loginform_frame, text="Student_ID", font=("Microsoft YaHei UI Light", 14), fg='black', bg='white')
    label_student_id.grid(row=1, column=0, padx=10, pady=5)

    entry_student_id = tk.Entry(loginform_frame)
    entry_student_id.grid(row=1, column=1, padx=10, pady=5)

    # Password Label and Entry
    label_password = tk.Label(loginform_frame, text="Password", font=("Microsoft YaHei UI Light", 14), fg='black', bg='white')
    label_password.grid(row=2, column=0, padx=10, pady=5)

    entry_password = tk.Entry(loginform_frame, show="*")
    entry_password.grid(row=2, column=1, padx=10, pady=5)

    def toggle_password():
        if entry_password.cget('show')== '':
            entry_password.config(show='*')
            toggle_button.config(text='show')
        else:
            entry_password.config(show='')
            toggle_button.config(text='hide')
            
        
    toggle_button = tk.Button(loginform_frame, text='Show', command=toggle_password)
    toggle_button.grid(row=2, column=2, padx=10, pady=5)

    # Function to handle submission
    def submit():
        student_id = entry_student_id.get()
        password = entry_password.get()

        if not student_id or not password:
            messagebox.showwarning("Input Error", "All fields are required.")
        else:
            # Verify user data from the SQLite database
            conn = sqlite3.connect('parking_system.db')
            c = conn.cursor()
            c.execute('''
                SELECT * FROM users WHERE user_id = ? AND password = ?
            ''', (student_id, password))
            user = c.fetchone()
            conn.close()

            if user:
                messagebox.showinfo("Login", "Login Successful!")
                student_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid Student ID or Password")

    # Forget Password Button
    button_forget = tk.Button(loginform_frame, text="Forget Password", font=("Microsoft YaHei UI Light", 8, 'bold'), fg='red', command=submit)
    button_forget.grid(row=3, column=1, sticky="e", pady=5, padx=10)

    # Submit Button
    button_submit = tk.Button(loginform_frame, text="Submit", font=("Microsoft YaHei UI Light", 16), fg='black', command=submit)
    button_submit.grid(row=4, columnspan=2, pady=10)
    
# Function to handle the guard login process
def button_guard_login():
    # Create a new top-level window for guard login form
    guard_login_window = tk.Toplevel(root)
    guard_login_window.title("GUARD LOGIN")
    guard_login_window.geometry('900x900')

    guard_bg_image = tk.PhotoImage(file=r"C:\Users\KARTHIGHAYINI\Downloads\WhatsApp-Image-2024-06-05-at-2.07.03-AM.png")
    guard_login_window.bg_image = guard_bg_image  # keep a reference to avoid garbage collection
    guard_bg_label = tk.Label(guard_login_window, image=guard_bg_image)
    guard_bg_label.place(relwidth=1, relheight=1)

    loginform_frame = tk.Frame(guard_login_window, bg='white', bd=10)
    loginform_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Guard heading text
    guard_heading = tk.Label(loginform_frame, text="GUARD LOGIN", font=("Microsoft YaHei UI Light", 23, 'bold'), fg='black', bg='white')
    guard_heading.grid(row=0, columnspan=2, pady=20)

    # Guard_ID Label and Entry
    label_guard_id = tk.Label(loginform_frame, text="Guard_ID", font=("Microsoft YaHei UI Light", 14), fg='black', bg='white')
    label_guard_id.grid(row=1, column=0, padx=10, pady=5)

    entry_guard_id = tk.Entry(loginform_frame)
    entry_guard_id.grid(row=1, column=1, padx=10, pady=5)

    # Password Label and Entry
    label_password = tk.Label(loginform_frame, text="Password", font=("Microsoft YaHei UI Light", 14), fg='black', bg='white')
    label_password.grid(row=2, column=0, padx=10, pady=5)

    entry_password = tk.Entry(loginform_frame, show="*")
    entry_password.grid(row=2, column=1, padx=10, pady=5)

    
    def toggle_password():
        if entry_password.cget('show')== '':
            entry_password.config(show='*')
            toggle_button.config(text='show')
        else:
            entry_password.config(show='')
            toggle_button.config(text='hide')
            
        
    toggle_button = tk.Button(loginform_frame, text='Show', command=toggle_password)
    toggle_button.grid(row=2, column=2, padx=10, pady=5)

    # Function to handle login submission
    def login():
        guard_id = entry_guard_id.get()
        password = entry_password.get()

        
        if not guard_id or not password:
            messagebox.showwarning("Input Error", "Both fields are required.")
        else:
            # Verify user data from the SQLite database
            conn = sqlite3.connect('parking_system.db')
            c = conn.cursor()
            c.execute('''
                SELECT * FROM users WHERE user_id = ? AND password = ?
            ''', (guard_id, password))
            user = c.fetchone()
            conn.close()

            if user:
                messagebox.showinfo("Login", "Login Successful!")
                guard_login_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid Guard ID or Password")
        
    # Submit Button
    button_submit = tk.Button(guard_login_window, text="LOGIN", command=login)
    button_submit.pack()

    # Login Button
    button_login = tk.Button(loginform_frame, text="LOGIN", font=("Microsoft YaHei UI Light", 16), fg='black', command=login)
    button_login.grid(row=3, columnspan=2, pady=10)

# Buttons for Sign Up, Student Login, and Guard Login
button_sign_up = tk.Button(root, text="SIGN UP", command=button_sign_up, **button_info)
button_sign_up.pack(pady=20)

button_student_login = tk.Button(root, text="STUDENT LOGIN", command=button_student_login, **button_info)
button_student_login.pack(pady=20)

button_guard_login = tk.Button(root, text="GUARD LOGIN", command=button_guard_login, **button_info)
button_guard_login.pack(pady=20)

root.mainloop()
