import tkinter as tk
from tkinter import messagebox
import sqlite3

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


# Create a table for vehicles
c.execute('''
    CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        vehicle_type TEXT NOT NULL,
        vehicle_number TEXT NOT NULL,
        parking_space INTEGER NOT NULL,
        faculty TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
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
    signup_window.geometry('900x900')

    signup_bg_image = tk.PhotoImage(file=r"/Users/vikassni_1304/Downloads/bluebackground.png")
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

# Function to handle the student login process
def button_student():
    # Create a new top-level window for login form
    student_window = tk.Toplevel(root)
    student_window.title('STUDENT LOGIN FORM')
    student_window.geometry('900x900')

    student_bg_image = tk.PhotoImage(file=r"/Users/vikassni_1304/Downloads/bluebackground.png")
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

                vehicle_info_window(student_id)  # Call vehicle_info_window with user_id
                choose_parking_space(student_id)  # Open choose parking space window after successful login
            else:
                messagebox.showerror("Error", "Invalid Student ID or Password")


    # Forget Password Button
    button_forget = tk.Button(loginform_frame, text="Forget Password", font=("Microsoft YaHei UI Light", 8, 'bold'), fg='red')

            else:
                messagebox.showerror("Error", "Invalid Student ID or Password")

    # Forget Password Button
    button_forget = tk.Button(loginform_frame, text="Forget Password", font=("Microsoft YaHei UI Light", 8, 'bold'), fg='red', command=submit)

    

def vehicle_info_window(user_id):
    # Create a new top-level window for vehicle information
    vehicle_window = tk.Toplevel(root)
    vehicle_window.title("Vehicle Information")
    vehicle_window.geometry('900x900')

    vehicle_bg_image = tk.PhotoImage(file=r"/Users/vikassni_1304/Downloads/bluebackground.png")
    vehicle_window.bg_image = vehicle_bg_image  # keep a reference to avoid garbage collection
    vehicle_bg_label = tk.Label(vehicle_window, image=vehicle_bg_image)
    vehicle_bg_label.place(relwidth=1, relheight=1)

    vehicle_form_frame = tk.Frame(vehicle_window, bg='white', bd=10)
    vehicle_form_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Vehicle Type Label and OptionMenu
    label_vehicle_type = tk.Label(vehicle_form_frame, text="Vehicle Type", font=("Microsoft YaHei UI Light", 14), fg='black', bg='white')
    label_vehicle_type.grid(row=0, column=0, padx=10, pady=5)

    vehicle_type = tk.StringVar(vehicle_form_frame)
    vehicle_type.set("Car")  # default value
    option_vehicle_type = tk.OptionMenu(vehicle_form_frame, vehicle_type, "Car", "Motor")
    option_vehicle_type.grid(row=0, column=1, padx=10, pady=5)

    # Vehicle Number Plate Label and Entry
    label_vehicle_number = tk.Label(vehicle_form_frame, text="Vehicle Number Plate", font=("Microsoft YaHei UI Light", 14), fg='black', bg='white')
    label_vehicle_number.grid(row=1, column=0, padx=10, pady=5)

    entry_vehicle_number = tk.Entry(vehicle_form_frame)
    entry_vehicle_number.grid(row=1, column=1, padx=10, pady=5)

    # Faculty Label and OptionMenu
    label_faculty = tk.Label(vehicle_form_frame, text="Faculty", font=("Microsoft YaHei UI Light", 14), fg='black', bg='white')
    label_faculty.grid(row=2, column=0, padx=10, pady=5)

    faculty = tk.StringVar(vehicle_form_frame)
    faculty.set("FCI")  # default value
    option_faculty = tk.OptionMenu(vehicle_form_frame, faculty, "FCI", "FOE", "Other")  # Add more faculties as needed
    option_faculty.grid(row=2, column=1, padx=10, pady=5)

    # Function to handle submission
    def submit_vehicle_info():
        v_type = vehicle_type.get()
        v_number = entry_vehicle_number.get()
        v_faculty = faculty.get()

        if not v_number:
            messagebox.showwarning("Input Error", "Vehicle Number Plate is required.")
        else:
            # Insert vehicle data into the SQLite database
            conn = sqlite3.connect('parking_system.db')
            c = conn.cursor()
            c.execute('''
                INSERT INTO vehicles (user_id, vehicle_type, vehicle_number, faculty) VALUES (?, ?, ?, ?)
            ''', (user_id, v_type, v_number, v_faculty))
            conn.commit()
            conn.close()
            messagebox.showinfo("Vehicle Information", "Vehicle Information Submitted Successfully!")
            vehicle_window.destroy()

    # Submit Button
    button_submit_vehicle = tk.Button(vehicle_form_frame, text="Submit", font=("Microsoft YaHei UI Light", 16), fg='black', command=submit_vehicle_info)
    button_submit_vehicle.grid(row=3, columnspan=2, pady=10)

# Function to let student choose parking space

# Function to let student choose parking space
def choose_parking_space(user_id):
    # Create a new top-level window for parking space selection
    space_selection_window = tk.Toplevel(root)
    space_selection_window.title('Choose Parking Space')
    space_selection_window.geometry('1500x1500')

    # Create a frame to hold the parking layout
    layout_frame = tk.Frame(space_selection_window, bg='white', bd=10)
    layout_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor='center')

    # Function to handle button clicks
    def reserve_space(space):
        messagebox.showinfo("Parking Space", f"Parking Space {space} reserved successfully!")

        # Here, you can add code to update the database with the selected parking space
        # For example, you can insert a record into the vehicles table with the user_id and selected parking space

    # Create buttons for each parking space
    for i in range(1, 51):
        button_text = f"Space {i}"
        button = tk.Button(layout_frame, text=button_text, font=("Arial", 10), width=10, height=4,
                           command=lambda i=i: reserve_space(i))
        row = (i - 1) // 5
        col = (i - 1) % 5
        button.grid(row=row, column=col, padx=10, pady=10)



# Create a button for student login
button_student = tk.Button(root, text="STUDENT", width=20, height=2, font=('Times New Roman', 18), command=button_student)
button_student.pack(pady=20)

# Create buttons for each functionality
button_sign_up = tk.Button(root, text="SIGN UP", **button_info, command=button_sign_up)
button_sign_up.pack(pady=20)

# Main loop to run the Tkinter application
root.mainloop()

root.mainloop()

