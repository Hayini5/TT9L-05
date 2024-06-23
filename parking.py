import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import re
from datetime import datetime
import os
from datetime import datetime, timedelta

# Connect to SQLite database
conn = sqlite3.connect('parking_system.db')
# Create a cursor object
c = conn.cursor()

#Placeholder for the database connection function
def get_db_connection():
    # Implement this function to connect to your database
    pass

# Placeholder for the logged-in student email
logged_in_student_email = "student@example.com"

# Create a table for student
c.execute('''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        vehicle_type TEXT,
        vehicle_number TEXT,
        gender_type TEXT NOT NULL
    )
''')

# Create a table for guard
c.execute('''
    CREATE TABLE IF NOT EXISTS guard (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        user_id TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        gender_type TEXT NOT NULL,
        faculty TEXT
    )
''')

# Create a table for reservation
c.execute('''
    CREATE TABLE IF NOT EXISTS reservation (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_email TEXT NOT NULL, 
        faculty TEXT NOT NULL,
        parking_space TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL
    )
''')

# Add the phone number column to the user table
try:
    c.execute('ALTER TABLE USER ADD COLUMN phone number TEXT UNIQUE NOT NULL')
    print("Column 'Phone number' added successfully.")
except sqlite3.OperationalError as e:
    print("Error:", e)

# Commit the changes and close the connection
conn.commit()
conn.close()

# Global variable to store the currently logged-in student's email
logged_in_student_email = None

# Function to get a database connection
def get_db_connection():
    return sqlite3.connect('parking_system.db')

# Function to validate MMU student email and validate NO KP
def validate_mmu_email(student_email):
    return re.match(r"^\d{10}@student\.mmu\.edu\.my$", student_email) is not None

def validate_guard_id(NO_KP):
    return re.match(r"^[A-Z]{2}-\d{3}$", NO_KP.upper()) is not None

test_id = " NS-111 "
if validate_guard_id(test_id):
    print(f"{test_id.strip()} is a valid ID.")
else:
    print(f"{test_id.strip()} is an invalid ID.")

def validate_phone_number(phone_number):
    # Define the regular expression pattern for a valid phone number
    pattern = r"^[0-9]{10,11}$"  # This pattern matches a string of exactly 10 or 11 digits
    # Use re.match to check if the phone number matches the pattern
    return bool(re.match(pattern, phone_number))

root = tk.Tk()
root.title('LOGIN')
root.geometry('900x900')

image_folder = os.path.join(os.path.dirname(__file__), 'images')
image_path = os.path.join(image_folder, 'IMAGE 1.png')

bg_image = tk.PhotoImage(file=image_path)
root.bg_image = bg_image  # keep a reference to avoid garbage collection

# Create a Label widget to display the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # stretch the label to fill the entire window



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
    signup_window.title("SIGN UP SELECTION")
    signup_window.geometry('900x900')

    image_folder = os.path.join(os.path.dirname(__file__), 'images')    
    signup_bg_image = tk.PhotoImage(file=os.path.join(image_folder, 'IMAGE 2.png'))
    signup_window.bg_image = signup_bg_image
    signup_bg_label = tk.Label(signup_window, image=signup_bg_image)
    signup_bg_label.place(relwidth=1, relheight=1)

    signupselection_frame = tk.Frame(signup_window, bg='black', bd=10)
    signupselection_frame.place(relx=0.5, rely=0.4, anchor='center')  # Adjust the rely parameter to move the frame up

    # Label and Entry
    label = tk.Label(signupselection_frame, text="ARE YOU A STUDENT OR A GUARD TO SIGN UP?", fg='black', bg='white', font=("Times New Roman", 16))
    label.grid(row=0, column=0, padx=10, pady=5)

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

    image_folder = os.path.join(os.path.dirname(__file__), 'images')   
    signup_bg_image = tk.PhotoImage(file=os.path.join(image_folder, 'IMAGE 2.png'))
    signup_window.bg_image = signup_bg_image
    signup_bg_label = tk.Label(signup_window, image=signup_bg_image)
    signup_bg_label.place(relwidth=1, relheight=1)

    signupform_frame = tk.Frame(signup_window, bg='black', bd=10)
    signupform_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Name Label and Entry
    label_name = tk.Label(signupform_frame, text="Name:", fg='black', bg='white')
    label_name.grid(row=0, column=0, padx=10, pady=5)

    entry_name = tk.Entry(signupform_frame)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    # Phone Number Label and Entry
    label_phone_number = tk.Label(signupform_frame, text="Phone Number:", fg='black', bg='white')
    label_phone_number.grid(row=1, column=0, padx=10, pady=5)

    entry_phone_number = tk.Entry(signupform_frame)
    entry_phone_number.grid(row=1, column=1, padx=10, pady=5)

    # Email Label and Entry
    label_email = tk.Label(signupform_frame, text=" MMU Email:", fg='black', bg='white')
    label_email.grid(row=2, column=0, padx=10, pady=5)

    entry_email = tk.Entry(signupform_frame)
    entry_email.grid(row=2, column=1, padx=10, pady=5)

    # Password Label and Entry
    label_password = tk.Label(signupform_frame, text="Password:", fg='black', bg='white')
    label_password.grid(row=3, column=0, padx=10, pady=5)

    entry_password = tk.Entry(signupform_frame, show="*")
    entry_password.grid(row=3, column=1, padx=10, pady=5)

    def toggle_password():
        if entry_password.cget('show')== '':
            entry_password.config(show='*')
            toggle_button.config(text='Show')
        else:
            entry_password.config(show='')
            toggle_button.config(text='Hide')
            
    toggle_button = tk.Button(signupform_frame, text='Show', command=toggle_password)
    toggle_button.grid(row=3, column=2, padx=10, pady=5)

    # Vehicle Type Label and OptionMenu
    label_vehicle_type = tk.Label(signupform_frame, text="Vehicle Type:", fg='black', bg='white')
    label_vehicle_type.grid(row=4, column=0, padx=10, pady=5)

    vehicle_type = tk.StringVar(signupform_frame)
    vehicle_type.set("Select")  # default value
    option_vehicle_type = tk.OptionMenu(signupform_frame, vehicle_type, "Car", "Motor")
    option_vehicle_type.grid(row=4, column=1, padx=10, pady=5)

    # Vehicle Number Plate Label and Entry
    label_vehicle_number = tk.Label(signupform_frame, text="Vehicle Number Plate:", fg='black', bg='white')
    label_vehicle_number.grid(row=5, column=0, padx=10, pady=5)

    entry_vehicle_number = tk.Entry(signupform_frame)
    entry_vehicle_number.grid(row=5, column=1, padx=10, pady=5)

    # Gender and OptionMenu
    gender_type_label = tk.Label(signupform_frame, text="Gender:", fg='black', bg='white')
    gender_type_label.grid(row=6, column=0, padx=10, pady=5)

    gender_type = tk.StringVar(signupform_frame)
    gender_type.set("Select")  # default value
    option_gender_type = tk.OptionMenu(signupform_frame, gender_type, "Female", "Male")
    option_gender_type.grid(row=6, column=1, padx=10, pady=5)
    
    # Function to handle submission
    def submit():
        name = entry_name.get()
        phone_number = entry_phone_number.get()
        email = entry_email.get()
        password = entry_password.get()
        v_type = vehicle_type.get()
        v_number = entry_vehicle_number.get()
        g_type = gender_type.get()

        if not name or not phone_number or not email or not password or not v_number or not v_type or not g_type:
            messagebox.showwarning("Input Error", "All fields are required.")
            signup_window.destroy()
            return student_sign_up()
        elif not validate_mmu_email(email):
            messagebox.showwarning("Input Error", "Invalid email address.")
            signup_window.destroy()
            return student_sign_up()
        elif not validate_phone_number(phone_number):
            messagebox.showwarning("Input Error", "Invalid phone number.")
        else:
            # Open a new connection for the submission
            conn = get_db_connection()
            c = conn.cursor()
            # Insert user data into the SQLite database
            try:
                c.execute('''
                INSERT INTO student (name, phone_number, email, password,  vehicle_type, vehicle_number, gender_type) VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (name, phone_number, email, password, v_type, v_number, g_type))
                conn.commit()  # Commit the changes to the database
                messagebox.showinfo("Sign Up", "Sign Up Successful!")
                signup_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Email already exists. Please choose a different one.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                conn.close()  # Ensure the connection is closed

    # Submit Button
    button_submit = tk.Button(signupform_frame, text="SIGN UP", command=submit)
    button_submit.grid(row=7, column=1, padx=10, pady=10)

# Function to display the users table
def display_users_table():
    # Connect to the SQLite database
    conn = sqlite3.connect('parking_system.db')
    c = conn.cursor()

    # Fetch all rows from the student table
    c.execute('SELECT * FROM student')
    users = c.fetchall()

    # Close the connection
    conn.close()

    # Create a new top-level window for displaying the users table
    display_window = tk.Toplevel(root)
    display_window.title('Users Table')
    display_window.geometry('900x900')

    # Create a treeview widget to display the users table
    tree = ttk.Treeview(display_window)
    tree["columns"] = ("Name", "Phone Number", "Email",  "Vehicle Number", "Vehicle Type")

    # Define column headings
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Name", anchor=tk.W, width=100)
    tree.column("Phone Number", anchor=tk.W, width=100)
    tree.column("Email", anchor=tk.W, width=200)
    tree.column("Vehicle Number", anchor=tk.W, width=100)
    tree.column("Vehicle Type", anchor=tk.W, width=100)
    

    # Define column headings
    tree.heading("#0", text="NO", anchor=tk.W)
    tree.heading("Name", text="Name", anchor=tk.W)
    tree.heading("Phone Number", text="Phone Number", anchor=tk.W)
    tree.heading("Email", text="Email", anchor=tk.W)
    tree.heading("Vehicle Number", text="Vehicle Number", anchor=tk.W)
    tree.heading("Vehicle Type", text="Vehicle Type", anchor=tk.W)
    

    # Insert data into the treeview
    for user in users:
        tree.insert("", "end", values=(user[1], user[2], user[3], user[4], user[5]))

    tree.pack()

def guard_sign_up():
    # Create a new top-level window for sign up form
    signup_window = tk.Toplevel(root)
    signup_window.title("SIGN UP FORM")
    signup_window.geometry('900x900')

    image_folder = os.path.join(os.path.dirname(__file__), 'images')    
    signup_bg_image = tk.PhotoImage(file=os.path.join(image_folder, 'IMAGE 2.png'))
    signup_window.bg_image = signup_bg_image
    signup_bg_label = tk.Label(signup_window, image=signup_bg_image)
    signup_bg_label.place(relwidth=1, relheight=1)


    signupform_frame = tk.Frame(signup_window, bg='black', bd=10)
    signupform_frame.place(relx=0.5, rely=0.5, anchor='center')

# Name Label and Entry
    label_name = tk.Label(signupform_frame, text="Name:", fg='black', bg='white')
    label_name.grid(row=0, column=0, padx=10, pady=5)

    entry_name = tk.Entry(signupform_frame)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    # ID Label and Entry
    label_id = tk.Label(signupform_frame, text="NO.PK:", fg='black', bg='white')
    label_id.grid(row=1, column=0, padx=10, pady=5)

    entry_id = tk.Entry(signupform_frame)
    entry_id.grid(row=1, column=1, padx=10, pady=5)

    # Password Label and Entry
    label_password = tk.Label(signupform_frame, text="Password:", fg='black', bg='white')
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
    
    # Gender and OptionMenu
    gender_type_label = tk.Label(signupform_frame, text="Gender:",  fg='black', bg='white')
    gender_type_label.grid(row=3, column=0, padx=10, pady=5)

    gender_type = tk.StringVar(signupform_frame)
    gender_type.set("select")  # default value
    option_gender_type = tk.OptionMenu(signupform_frame, gender_type, "Female", "Male")
    option_gender_type.grid(row=3, column=1, padx=10, pady=5)

     # Faculty and Entry
    faculty_label = tk.Label(signupform_frame, text="Faculty:", fg='black', bg='white')
    faculty_label.grid(row=4, column=0, padx=10, pady=5)

    faculty_entry = tk.Entry(signupform_frame)
    faculty_entry.grid(row=4, column=1, padx=10, pady=5)

    # Function to handle submission
    def submit():
        name = entry_name.get()
        guard_id = entry_id.get()
        password = entry_password.get()
        g_type = gender_type.get()
        faculty = faculty_entry.get()

        if not name or not guard_id or not password or not g_type or not faculty:
            messagebox.showwarning("Input Error", "All fields are required.")
            signup_window.destroy()
            return guard_sign_up()
        elif not validate_guard_id(guard_id):
            messagebox.showwarning("Input Error", "Invalid Guard ID. Please enter a valid ID")
            signup_window.destroy()
            return guard_sign_up()
        else:
            # Insert user data into the SQLite database
            try:
                conn = sqlite3.connect('parking_system.db')
                c = conn.cursor()
                c.execute('''
                    INSERT INTO guard (name, user_id, password, gender_type, faculty) VALUES (?, ?, ?, ?, ?)
                ''', (name, guard_id, password, g_type, faculty))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sign Up", "Sign Up Successful!")
                signup_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Guard ID already exists. Please choose a different one.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    # Submit Button
    button_submit = tk.Button(signupform_frame, text="Submit", command=submit)
    button_submit.grid(row=5, column=1, padx=10, pady=10)

#Function to handle the forget password button
def forget_password():
    # Create a new top-level window for password reset
    forget_window = tk.Toplevel(root)
    forget_window.title('FORGOT PASSWORD')
    forget_window.geometry('300x200')

    # Create a frame to hold the form
    frame = tk.Frame(forget_window, bg='white', bd=10)
    frame.place(relx=0.5, rely=0.5, anchor='center')
   
    # Email Label and Entry
    label_email = tk.Label(frame, text="Enter your Email:", font=("Times New Roman", 13,), fg='black', bg='white')
    label_email.grid(row=0, column=0, padx=10, pady=5)

    entry_email = tk.Entry(frame, font=("Times New Roman", 10,), fg='black', bg='white' )
    entry_email.grid(row=0, column=1, padx=10, pady=5)

    # Function to handle password reset
    def reset_password():
        email = entry_email.get()

        if not email:
            messagebox.showwarning("Input Error", "Email field is required.")
            return

        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT password FROM student WHERE email = ?', (email,))
        result = c.fetchone()
        conn.close()

        if result:
            password = result[0]
            messagebox.showinfo("Password Reset", f"Your password is: {password}")
            forget_window.destroy()
        else:
            messagebox.showerror("Error", "No account found with this email.")

    # Submit Button
    button_submit = tk.Button(frame, text="SUBMIT", font=("Times New Roman", 12), fg='red', command=reset_password)
    button_submit.grid(row=1, columnspan=2, pady=10)

# Function to handle the student login process
def student_login():
    global logged_in_student_email  # Declare as global to modify the global variable

    # Create a new top-level window for login form
    student_window = tk.Toplevel(root)
    student_window.title('STUDENT LOGIN FORM')
    student_window.geometry('900x900')

    image_folder = os.path.join(os.path.dirname(__file__), 'images')    
    student_bg_image = tk.PhotoImage(file=os.path.join(image_folder, 'IMAGE 2.png'))
    student_window.bg_image = student_bg_image
    student_bg_label = tk.Label(student_window, image=student_bg_image)
    student_bg_label.place(relwidth=1, relheight=1)



    # Create a frame to hold the login form
    loginform_frame = tk.Frame(student_window, bg='white', bd=10)
    loginform_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Student heading text
    student_heading = tk.Label(loginform_frame, text="STUDENT LOGIN", font=("Microsoft YaHei UI Light", 23, 'bold'), fg='black', bg='white')
    student_heading.grid(row=0, columnspan=2, pady=20)

    # Student_email Label and Entry
    label_student_email = tk.Label(loginform_frame, text="Student_Email:", font=("Microsoft YaHei UI Light", 14), fg='black', bg='white')
    label_student_email.grid(row=1, column=0, padx=10, pady=5)

    entry_student_email = tk.Entry(loginform_frame)
    entry_student_email.grid(row=1, column=1, padx=10, pady=5)

    # Password Label and Entry
    label_password = tk.Label(loginform_frame, text="Password:", font=("Microsoft YaHei UI Light", 14), fg='black', bg='white')
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
        student_email = entry_student_email.get()
        password = entry_password.get()

        if not student_email or not password:
            messagebox.showwarning("Input Error", "All fields are required.")
            student_window.destroy()
            return student_login()
        else:
            conn = sqlite3.connect('parking_system.db')
            c = conn.cursor()
            c.execute('''
                SELECT * FROM student WHERE email = ? AND password = ?
            ''', (student_email, password))
            result = c.fetchone()
            conn.close()
            if result:
                global logged_in_student_email
                logged_in_student_email = student_email  # Store the logged-in student's email
                messagebox.showinfo("Login", "Login Successful!")
                student_window.destroy()
                # Call parking_system function after displaying user information
                parking_system()
            else:
                messagebox.showerror("Login Error", "Invalid User Email or Password")

    # Submit Button
    button_submit = tk.Button(loginform_frame, text="LOGIN", font=("Microsoft YaHei UI Light", 16), fg='Red', command=submit)
    button_submit.grid(row=4, columnspan=2, pady=10)

    # Function to handle the booking, cancelation and extension
def parking_system():
    # Create a new top-level window for parking system
    parking_system_window = tk.Toplevel(root)
    parking_system_window.title("Parking Confirmation")
    parking_system_window.geometry('900x900')

    image_folder = os.path.join(os.path.dirname(__file__), 'images')
    parking_system_window_bg_image = tk.PhotoImage(file=os.path.join(image_folder, 'IMAGE 1.png'))
    parking_system_window.bg_image = parking_system_window_bg_image
    parking_system_window_bg_label = tk.Label(parking_system_window, image=parking_system_window_bg_image)
    parking_system_window_bg_label.place(relwidth=1, relheight=1)

    # Create a new frame for the buttons
    button_frame = tk.Frame(parking_system_window, bg='black', bd=10)
    button_frame.place(relx=0.5, rely=0.6, anchor='center')  # Adjust the rely parameter to move the frame down

    # Create a button to handle booking
    book_button = tk.Button(parking_system_window, text="PARKING RESERVATION",  width=20, height=2, font=('Times New Roman', 18), command=open_booking_window)
    book_button.pack(pady=30)

    # Fuction to handle the booking process
def open_booking_window():
    # Create a new top-level-window for book form
    book_window = tk.Toplevel(root)
    book_window.title("BOOKING")
    book_window.geometry('900x900')

    book_bg_image = tk.PhotoImage(file=r"images/IMAGE 1.png")
    book_window.bg_image = book_bg_image  # keep a reference to avoid garbage collection
    book_bg_label = tk.Label(book_window, image=book_bg_image)
    book_bg_label.place(relwidth=1, relheight=1)
    
    bookselection_frame = tk.Frame(book_window, bg='white', bd=10)
    bookselection_frame.place(relx=0.5, rely=0.1, anchor='center')  # Adjust the rely parameter to move the frame up
    
    # Label
    label = tk.Label(bookselection_frame, text="CHOOSE YOUR PARKING AREA", fg='black', bg='white', font=("Times New Roman", 14))
    label.grid(row=0, column=0, padx=10, pady=4)

    # Create a new frame for the buttons
    button_frame = tk.Frame(book_window, bg='white', bd=10)
    button_frame.place(relx=0.5, rely=0.2, anchor='center')  # Adjust the rely parameter to move the frame down
     
    # Example buttons for different parking areas
    button_user1 = tk.Button(button_frame, text="FCI", width=20, height=2, font=('Times New Roman', 12), command=fci_layout)
    button_user1.grid(row=0, column=0, padx=6, pady=6)

    button_user2 = tk.Button(button_frame, text="FOE", width=20, height=2, font=('Times New Roman', 12), command=foe_layout)
    button_user2.grid(row=0, column=1, padx=6, pady=6)

def fci_layout():
    # Create a new top-level window for parking space selection
    space_selection_window = tk.Toplevel(root)
    space_selection_window.title('Choose Parking Space')
    space_selection_window.geometry('900x900')

    # Create a frame to hold the parking layout
    layout_frame = tk.Frame(space_selection_window, bg='blue', bd=10)
    layout_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Dictionary to store button references 
    button_dict ={}

    # Function to get the end time of the student's current reservation
    def get_current_end_time():
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT end_time FROM reservation WHERE faculty='FCI' AND student_email=?", (logged_in_student_email,))
        end_time = c.fetchone()
        conn.close()
        return end_time[0] if end_time else None
    
    def cancellation(space):
        # Check if the user reserved the space or not
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM reservation WHERE parking_space = ?", (space,))
        reservation_data = c.fetchone()
        conn.close()

        if reservation_data[1] == logged_in_student_email:
            # Create a new top-level window for cancelling reservation
            action_window = tk.Toplevel(space_selection_window)
            action_window.title('Cancel or Extend reservation')
            action_window.geometry('400x200')

            # Define a grid
            action_window.columnconfigure((0,1,2,3,4), weight=1)
            action_window.rowconfigure((0,1,2,3), weight=1)

            # Function to cancel the reservation
            def cancel():
                conn = get_db_connection()
                c = conn.cursor()
                c.execute("DELETE FROM reservation WHERE parking_space = ?", (space,))
                messagebox.showinfo("Success", "Parking reservation is cancelled successfully.")
                conn.commit()
                conn.close()
                action_window.destroy() # Close the cancellation window after reservation is cancelled

            # Function to extend the reservation
            def extend():
                extend_window = tk.Toplevel(action_window)
                extend_window.title('Extend Reservation')
                extend_window.geometry('400x200')

                label = tk.Label(extend_window, text="Choose extension duration")
                label.pack()

                def update_end_time(minutes):
                    current_end_time = datetime.strptime(get_current_end_time(), "%H:%M")
                    new_end_time = current_end_time + timedelta(minutes=minutes)
                    conn = get_db_connection()
                    c = conn.cursor()
                    c.execute("UPDATE reservation SET end_time = ? WHERE parking_space = ?", (new_end_time.strftime("%H:%M"), space))
                    conn.commit()
                    conn.close()
                  
                    messagebox.showinfo("Success", "Parking reservation is extended successfully.")
                    extend_window.destroy()
                    action_window.destroy()

                
                                        
                    
                button_1_hour = tk.Button(extend_window, text="1 Hour", command=lambda: update_end_time(60))
                button_1_hour.pack(pady=10)
                button_30_minutes = tk.Button(extend_window, text="30 Minutes", command=lambda: update_end_time(30))
                button_30_minutes.pack(pady=10)

            label = tk.Label(action_window, text="Would you like to cancel or extend your reservation?", font=("Arial", 12))
            label.grid(row=1, column=1, columnspan=3)

            cancel_button = tk.Button(action_window, text="Cancel", bg='light grey', font=("Arial", 10), command=cancel)
            cancel_button.grid(row=2, column=1, sticky='ew')

            extend_button = tk.Button(action_window, text="Extend", bg='light grey', font=("Arial", 10), command=extend)
            extend_button.grid(row=2, column=3, sticky='ew')

        

        else:
            messagebox.showerror("Error", "Parking space is already reserved by another student.")
            button_dict[space].config(state='disabled')
            return
        
            

    # Function to handle button clicks
    def reserve_space(space, button_dict):
        current_end_time = get_current_end_time()
        if current_end_time:
            current_time = datetime.now().strftime('%H:%M')
            if current_time < current_end_time:
                messagebox.showerror("Error", "You already have a current reservation. Please wait until it ends.")
                return
        
        # Check if the student has an existing reservation in FOE
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM reservation WHERE faculty='FOE' AND student_email=?", (logged_in_student_email,))
        if c.fetchone():
            messagebox.showerror("Error", "You already have a reservation in FOE. You cannot book a space in FCI.")
            return
        
        # Check if the parking space is already reserved by another student
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM reservation WHERE faculty='FCI' AND parking_space=? AND student_email!=?", (space,logged_in_student_email))
        if c.fetchone():
            messagebox.showerror("Error", "Parking space is already reserved by another student.")
            button_dict[space].config(state='disabled')
            return

        # Create a new window for time selection
        time_selection_window = tk.Toplevel(space_selection_window)
        time_selection_window.title('Select Time')
        time_selection_window.geometry('300x200')

        # Time selection labels
        time_label1= tk.Label(time_selection_window, text= "Start Time:", bg='blue', font=("Microsoft YaHei UI Light", 10), fg='white')
        time_label1.grid(row=0, column=0, padx=10, pady=10)

        time_label2= tk.Label(time_selection_window, text= "End Time:", bg='blue', font=("Microsoft YaHei UI Light", 10), fg='white')
        time_label2.grid(row=1, column=0, padx=10, pady=10)

        # List of times
        times = [f"{hour}:00" for hour in range (24)]

        # Variable to store selected times
        start_time = tk.StringVar(time_selection_window)
        start_time.set(times[0])  # default value

        end_time = tk.StringVar(time_selection_window)
        end_time.set(times[0])  # default value

        # Create OptionMenu for time selection
        start_time_menu = tk.OptionMenu(time_selection_window, start_time, *times)
        start_time_menu.grid(row=0, column=1, padx=10, pady=10)

        end_time_menu = tk.OptionMenu(time_selection_window, end_time, *times)
        end_time_menu.grid(row=1, column=1, padx=10, pady=10)

        # Label to show confirmation message
        confirmation_label = tk.Label(time_selection_window, text="**Duration of parking cannot exceed 5 hours", bg='red', font=("Microsoft YaHei UI Light", 8), fg='white')
        confirmation_label.grid(row=2, columnspan=3, padx=10, pady=10)

        # Function to check if the selected duration is within the 5-hour limit
        def check_duration(start, end):
            start_hour = int(start.split(":")[0])
            end_hour = int(end.split(":")[0])
            if start_hour <= end_hour:
                duration = end_hour - start_hour
            else:
                duration = (24 - start_hour) + end_hour
            return duration <= 5

        # Function to confirm reservation with selected time
        def confirm_reservation():
            chosen_parking_space = space
            chosen_start_time = start_time.get()
            chosen_end_time = end_time.get()

            # Check if both start time and end time are selected
            if not chosen_start_time or not chosen_end_time:
                messagebox.showerror("Error", "Please select both the start time and end time.")
                return

            # Check if either start or end time is "0:00"
            if chosen_start_time == "0:00" or chosen_end_time == "0:00":
                messagebox.showerror("Error", "Start time and end time cannot be 0:00.")
                return

            # Check if the duration exceeds 5 hours
            if check_duration(chosen_start_time, chosen_end_time):
                # Check if the student has an existing reservation in FOE with the same time
                conn = get_db_connection()
                c = conn.cursor()
                
                # Insert parking into the database
                try:
                    c.execute("INSERT INTO reservation (student_email, faculty, parking_space, start_time, end_time) VALUES (?,?,?,?,?)", 
                              (logged_in_student_email, 'FCI', chosen_parking_space, chosen_start_time, chosen_end_time))
                    conn.commit()
                    messagebox.showinfo("Success", "Parking space reserved successfully.")
                    button_dict[space].config(bg='red', text=f"Space {space}\nReserved") #change button colour to red and update the text
                    time_selection_window.destroy()

                except sqlite3.Error as e:
                    messagebox.showerror("Error", "Failed to reserve parking space. Error: " + str(e))
                finally:
                    conn.close()

        # Confirm button
        confirm_button = tk.Button(time_selection_window, text="RESERVED",bg='blue', font=("Microsoft YaHei UI Light", 10), fg='white', command=confirm_reservation)
        confirm_button.grid(row=3, columnspan=3, pady=20)

    # Create buttons for each parking space
    for i in range(1, 51):
        button_text = f"Space {i}"
        c = get_db_connection().cursor()
        c.execute(f"SELECT * FROM reservation WHERE faculty='FCI' AND parking_space=?", (i,))
        # Check if the button is already reserved
        if c.fetchone():
            button = tk.Button(layout_frame, text=f"Space {i}\nReserved", font=("Arial", 10), width=10, height=2,bg='red', command=lambda i=i: cancellation(i))
        else:
           button = tk.Button(layout_frame, text=f"Space {i}", font=("Arial", 10), width=10, height=2,
                           command=lambda i=i, button_dict=button_dict: reserve_space(i, button_dict))
        row = (i - 1) // 10
        col = (i - 1) % 10
        button.grid(row=row, column=col, padx=5, pady=5)
        button_dict[i] = button #Store button reference in dictionary

    # Function to update button states
    def update_button_states():
        
        current_time = datetime.now().strftime('%H:%M')
        for space, end_time in reserved_spaces:
            end_time_dt = datetime.strptime(end_time, '%H:%M').time()
            current_time_dt = datetime.strptime(current_time, '%H:%M').time()

        if current_time_dt < end_time_dt:
            button_dict[int(space)].config(bg='yellow', text=f"Space {space}\nReserved", state='normal', command=lambda i=i: cancellation(i))
        else:
            button_dict[int(space)].config(state='normal', bg='blue', text=f"Space {space}")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT parking_space FROM reservation WHERE faculty='FCI'")
        reserved_spaces = [row[0] for row in c.fetchall()]
        for space in reserved_spaces:
            button_dict[int(space)].config(bg='red', text="Reserved")

    # Update button states when the window is opened
    update_button_states()

    # Function to refresh the layout and disable already reserved spaces
    def refresh_layout():
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT parking_space, end_time FROM reservation WHERE faculty = "FCI"')
        reserved_spaces = c.fetchall()
        conn.close()

        current_time = datetime.now().strftime('%H:%M')
        for space, end_time in reserved_spaces:
            end_time_dt = datetime.strptime(end_time, '%H:%M').time()
            current_time_dt = datetime.strptime(current_time, '%H:%M').time()

            if current_time_dt < end_time_dt:
                button_dict[int(space)].config(state='disabled', bg='yellow', text=f"Space {space}\nReserved")
            else:
                button_dict[int(space)].config(state='normal', bg='blue', text=f"Space {space}")

        # Schedule the function to run again after 24 hours (86400000 milliseconds)
        layout_frame.after(86400000, refresh_layout)

    # Call the refresh_layout function to disable already reserved spaces and keep updating every minute
    refresh_layout()

    
# Function to let student choose parking space
def foe_layout():
    # Create a new top-level window for parking space selection
    space_selection_window = tk.Toplevel(root)
    space_selection_window.title('Choose Parking Space')
    space_selection_window.geometry('900x900')

    # Create a frame to hold the parking layout
    layout_frame = tk.Frame(space_selection_window, bg='green', bd=10)
    layout_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Dictionary to store button references 
    button_dict ={}

    # Function to get the end time of the student's current reservation
    def get_current_end_time():
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT end_time FROM reservation WHERE faculty='FOE' AND student_email=?", (logged_in_student_email,))
        end_time = c.fetchone()
        conn.close()
        return end_time[0] if end_time else None
    
    def cancellation(space):
        # Check if the user reserved the space or not
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM reservation WHERE parking_space = ?", (space,))
        reservation_data = c.fetchone()
        conn.close()

        if reservation_data[1] == logged_in_student_email:
            # Create a new top-level window for cancelling reservation
            action_window = tk.Toplevel(space_selection_window)
            action_window.title('Cancel reservation')
            action_window.geometry('400x200')

            # Define a grid
            action_window.columnconfigure((0,1,2,3,4), weight=1)
            action_window.rowconfigure((0,1,2,3), weight=1)

            # Function to cancel the reservation
            def cancel():
                conn = get_db_connection()
                c = conn.cursor()
                c.execute("DELETE FROM reservation WHERE parking_space = ?", (space,))
                messagebox.showinfo("Success", "Parking reservation is cancelled successfully.")
                conn.commit()
                conn.close()
                action_window.destroy() # Close the cancellation window after reservation is cancelled

            # Function to extend the reservation
            def extend():
                extend_window = tk.Toplevel(action_window)
                extend_window.title('Extend Reservation')
                extend_window.geometry('400x200')

                label = tk.Label(extend_window, text="Choose extension duration")
                label.pack()

                def update_end_time(minutes):
                    current_end_time = datetime.strptime(get_current_end_time(), "%H:%M")
                    new_end_time = current_end_time + timedelta(minutes=minutes)
                    conn = get_db_connection()
                    c = conn.cursor()
                    c.execute("UPDATE reservation SET end_time = ? WHERE parking_space = ?", (new_end_time.strftime("%H:%M"), space))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Parking reservation is extended successfully.")
                    extend_window.destroy()
                    action_window.destroy()

                button_1_hour = tk.Button(extend_window, text="1 Hour", command=lambda: update_end_time(60))
                button_1_hour.pack(pady=10)
                button_30_minutes = tk.Button(extend_window, text="30 Minutes", command=lambda: update_end_time(30))
                button_30_minutes.pack(pady=10)

            label = tk.Label(action_window, text="Would you like to cancel or extend your reservation?", font=("Arial", 12))
            label.grid(row=1, column=1, columnspan=3)

            cancel_button = tk.Button(action_window, text="Cancel", bg='light grey', font=("Arial", 10), command=cancel)
            cancel_button.grid(row=2, column=1, sticky='ew')

            extend_button = tk.Button(action_window, text="Extend", bg='light grey', font=("Arial", 10), command=extend)
            extend_button.grid(row=2, column=3, sticky='ew')

        else:
            messagebox.showerror("Error", "Parking space is already reserved by another student.")
            button_dict[space].config(state='disabled')

    # Function to handle button clicks
    def reserve_space(space, button_dict):
        current_end_time = get_current_end_time()
        if current_end_time:
            current_time = datetime.now().strftime('%H:%M')
            if current_time < current_end_time:
                messagebox.showerror("Error", "You already have a current reservation. Please wait until it ends.")
                return
        
        # Check if the student has an existing reservation in FCI
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM reservation WHERE faculty='FCI' AND student_email=?", (logged_in_student_email,))
        if c.fetchone():
            messagebox.showerror("Error", "You already have a reservation in FCI. You cannot book a space in FOE.")
            return

        # Check if the parking space is already reserved by another student
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM reservation WHERE faculty='FOE' AND parking_space=? AND student_email!=?", (space,logged_in_student_email))
        if c.fetchone():
            messagebox.showerror("Error", "Parking space is already reserved by another student.")
            button_dict[space].config(state='disabled')
            return

        # Create a new window for time selection
        time_selection_window = tk.Toplevel(space_selection_window)
        time_selection_window.title('Select Time')
        time_selection_window.geometry('300x200')

        # Time selection labels
        time_label1= tk.Label(time_selection_window, text= "Start Time:", bg='green', font=("Microsoft YaHei UI Light", 10), fg='white')
        time_label1.grid(row=0, column=0, padx=10, pady=10)

        time_label2= tk.Label(time_selection_window, text= "End Time:", bg='green', font=("Microsoft YaHei UI Light", 10), fg='white')
        time_label2.grid(row=1, column=0, padx=10, pady=10)

        # List of times
        times = [f"{hour}:00" for hour in range (24)]

        # Variable to store selected times
        start_time = tk.StringVar(time_selection_window)
        start_time.set(times[0])  # default value

        end_time = tk.StringVar(time_selection_window)
        end_time.set(times[0])  # default value

        # Create OptionMenu for time selection
        start_time_menu = tk.OptionMenu(time_selection_window, start_time, *times)
        start_time_menu.grid(row=0, column=1, padx=10, pady=10)

        end_time_menu = tk.OptionMenu(time_selection_window, end_time, *times)
        end_time_menu.grid(row=1, column=1, padx=10, pady=10)

        # Label to show confirmation message
        confirmation_label = tk.Label(time_selection_window, text="**Duration of parking cannot exceed 5 hours", bg='red', font=("Microsoft YaHei UI Light", 8), fg='white')
        confirmation_label.grid(row=2, columnspan=3, padx=10, pady=10)

        # Function to check if the selected duration is within the 5-hour limit
        def check_duration(start, end):
            start_hour = int(start.split(":")[0])
            end_hour = int(end.split(":")[0])
            if start_hour <= end_hour:
                duration = end_hour - start_hour
            else:
                duration = (24 - start_hour) + end_hour
            return duration <= 5

        # Function to confirm reservation with selected time
        def confirm_reservation():
            chosen_parking_space = space
            chosen_start_time = start_time.get()
            chosen_end_time = end_time.get()

            # Check if both start time and end time are selected
            if not chosen_start_time or not chosen_end_time:
                messagebox.showerror("Error", "Please select both the start time and end time.")
                return

            # Check if either start or end time is "0:00"
            if chosen_start_time == "0:00" or chosen_end_time == "0:00":
                messagebox.showerror("Error", "Start time and end time cannot be 0:00.")
                return

            # Check if the duration exceeds 5 hours
            if check_duration(chosen_start_time, chosen_end_time):
                # Check if the student has an existing reservation in FCI with the same time
                conn = get_db_connection()
                c = conn.cursor()
                
                # Insert parking into the database
                try:
                    c.execute("INSERT INTO reservation (student_email, faculty, parking_space, start_time, end_time) VALUES (?,?,?,?,?)", 
                              (logged_in_student_email, 'FOE', chosen_parking_space, chosen_start_time, chosen_end_time))
                    conn.commit()
                    messagebox.showinfo("Success", "Parking space reserved successfully.")
                    button_dict[space].config(bg='red', text=f"Space {space}\nReserved") #change button colour to red and update the text
                    time_selection_window.destroy()
                    
                except sqlite3.Error as e:
                    messagebox.showerror("Error", "Failed to reserve parking space. Error: " + str(e))
                finally:
                    conn.close()

        # Confirm button
        confirm_button = tk.Button(time_selection_window, text="RESERVED",bg='green', font=("Microsoft YaHei UI Light", 10), fg='white', command=confirm_reservation)
        confirm_button.grid(row=3, columnspan=3, pady=20)

    # Create buttons for each parking space
    for i in range(1, 51):
        button_text = f"Space {i}"
        c = get_db_connection().cursor()
        c.execute(f"SELECT * FROM reservation WHERE faculty='FOE' AND parking_space=?", (i,))
        # Check if the button is already reserved
        if c.fetchone():
            button = tk.Button(layout_frame, text=f"Space {i}\nReserved", font=("Arial", 10), width=10, height=2,bg='red', command=lambda i=i: cancellation(i))
        else:
           button = tk.Button(layout_frame, text=f"Space {i}", font=("Arial", 10), width=10, height=2,
                           command=lambda i=i, button_dict=button_dict: reserve_space(i, button_dict))
        row = (i - 1) // 10
        col = (i - 1) % 10
        button.grid(row=row, column=col, padx=5, pady=5)
        button_dict[i] = button #Store button reference in dictionary

    # Function to update button states
    def update_button_states():
        
        current_time = datetime.now().strftime('%H:%M')
        for space, end_time in reserved_spaces:
            end_time_dt = datetime.strptime(end_time, '%H:%M').time()
            current_time_dt = datetime.strptime(current_time, '%H:%M').time()

        if current_time_dt < end_time_dt:
            button_dict[int(space)].config(bg='yellow', text=f"Space {space}\nReserved", command=lambda i=i: cancellation(i))
        else:
            button_dict[int(space)].config(state='normal', bg='blue', text=f"Space {space}")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT parking_space FROM reservation WHERE faculty='FOE'")
        reserved_spaces = [row[0] for row in c.fetchall()]
        for space in reserved_spaces:
            button_dict[int(space)].config(bg='red', text="Reserved")

    # Update button states when the window is opened
    update_button_states()

    # Function to refresh the layout and disable already reserved spaces
    def refresh_layout():
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT parking_space, end_time FROM reservation WHERE faculty = "FOE"')
        reserved_spaces = c.fetchall()
        conn.close()

        current_time = datetime.now().strftime('%H:%M')
        for space, end_time in reserved_spaces:
            end_time_dt = datetime.strptime(end_time, '%H:%M').time()
            current_time_dt = datetime.strptime(current_time, '%H:%M').time()

            if current_time_dt < end_time_dt:
                button_dict[int(space)].config(state='disabled', bg='yellow', text=f"Space {space}\nReserved")
            else:
                button_dict[int(space)].config(state='normal', bg='green', text=f"Space {space}")

        # Schedule the function to run again after 24 hours (86400000 milliseconds)
        layout_frame.after(86400000, refresh_layout)

    # Call the refresh_layout function to disable already reserved spaces and keep updating every minute
    refresh_layout()
    

def display_reservation_table():
    # Connect to the SQLite database
    conn = sqlite3.connect('parking_system.db')
    c = conn.cursor()

    # Fetch all rows from the reservation table
    c.execute('SELECT student_email, faculty, parking_space, start_time, end_time FROM reservation')
    users = c.fetchall()

    # Close the cursor and the connection
    c.close()
    conn.close()

    # Create a new top-level window for displaying the reservation table
    display_window = tk.Toplevel(root)
    display_window.title('Reservation Table')
    display_window.geometry('900x900')

    # Create a treeview widget to display the reservation table
    tree = ttk.Treeview(display_window)
    tree["columns"] = ("Student Email", "Faculty", "Parking Space", "Start Time", "End Time")

    # Define column headings
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Student Email", anchor=tk.W, width=200)
    tree.column("Faculty", anchor=tk.W, width=100)
    tree.column("Parking Space", anchor=tk.W, width=100)
    tree.column("Start Time", anchor=tk.W, width=100)
    tree.column("End Time", anchor=tk.W, width=100)

    # Define column headings
    tree.heading("#0", text="NO", anchor=tk.W)
    tree.heading("Student Email", text="Student Email", anchor=tk.W)
    tree.heading("Faculty", text="Faculty", anchor=tk.W)
    tree.heading("Parking Space", text="Parking Space", anchor=tk.W)
    tree.heading("Start Time", text="Start Time", anchor=tk.W)
    tree.heading("End Time", text="End Time", anchor=tk.W)

    # Insert data into the treeview
    for user in users:
        tree.insert("", "end", values=(user[0], user[1], user[2], user[3], user[4]))

    tree.pack()
    
    # Function to handle the guard login process
def guard_login():
    # Create a new top-level window for guard login form
    guard_login_window = tk.Toplevel(root)
    guard_login_window.title("GUARD LOGIN")
    guard_login_window.geometry('900x900')

    image_folder = os.path.join(os.path.dirname(__file__), 'images')    
    guard_login_window_bg_image = tk.PhotoImage(file=os.path.join(image_folder, 'IMAGE 2.png'))
    guard_login_window.bg_image = guard_login_window_bg_image
    guard_login_window_bg_label = tk.Label(guard_login_window, image=guard_login_window_bg_image)
    guard_login_window_bg_label.place(relwidth=1, relheight=1)


    loginform_frame = tk.Frame(guard_login_window, bg='white', bd=10)
    loginform_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Guard heading text
    guard_heading = tk.Label(loginform_frame, text="GUARD LOGIN", font=("Microsoft YaHei UI Light", 23, 'bold'), fg='black', bg='white')
    guard_heading.grid(row=0, columnspan=2, pady=20)

    # Guard_ID Label and Entry
    label_guard_id = tk.Label(loginform_frame, text="NO.PK:", font=("Microsoft YaHei UI Light", 14), fg='black', bg='white')
    label_guard_id.grid(row=1, column=0, padx=10, pady=5)

    entry_guard_id = tk.Entry(loginform_frame)
    entry_guard_id.grid(row=1, column=1, padx=10, pady=5)
   
    # Password Label and Entry
    label_password = tk.Label(loginform_frame, text="Password:", font=("Microsoft YaHei UI Light", 14), fg='black', bg='white')
    label_password.grid(row=2, column=0, padx=10, pady=5)

    entry_password = tk.Entry(loginform_frame, show="*")
    entry_password.grid(row=2, column=1, padx=10, pady=5)

    def toggle_password():
        if entry_password.cget('show')== '':
            entry_password.config(show='*')
            toggle_button.config(text='Show')
        else:
            entry_password.config(show='')
            toggle_button.config(text='Hide')
            
    toggle_button = tk.Button(loginform_frame, text='Show', command=toggle_password)
    toggle_button.grid(row=2, column=2, padx=10, pady=5)


     # Function to handle login submission
    def login():
        guard_id = entry_guard_id.get()
        password = entry_password.get()

        
        if not guard_id or not password:
            messagebox.showwarning("Input Error", "Both fields are required.")
            guard_login_window.destroy()
            return guard_login()
        else:
            # Verify user data from the SQLite database
            conn = sqlite3.connect('parking_system.db')
            c = conn.cursor()
            c.execute('''
                SELECT * FROM guard WHERE user_id = ? AND password = ?
            ''', (guard_id, password))
            user = c.fetchone()
            conn.close()

            if user:
                messagebox.showinfo("Login", "Login Successful!")
                guard_login_window.destroy()
                # Call parking_checking function after displaying user information
                parking_checking()
            else:
                messagebox.showerror("Error", "Invalid Guard ID or Password")
    # Login Button
    button_login = tk.Button(loginform_frame, text="LOGIN", font=("Microsoft YaHei UI Light", 16), fg='red', command=login)
    button_login.grid(row=4, columnspan=2, pady=10)
    
    
# Function to handle the data, fci layout and foe layout
def parking_checking():
    # Create a new top-level window for parking checking
    parking_checking_window = tk.Toplevel(root)
    parking_checking_window.title("Parking Checking")
    parking_checking_window.geometry('900x900')

    image_folder = os.path.join(os.path.dirname(__file__), 'images')    
    parking_checking_window_bg_image = tk.PhotoImage(file=os.path.join(image_folder, 'IMAGE 2.png'))
    parking_checking_window.bg_image = parking_checking_window_bg_image
    parking_checking_window_bg_label = tk.Label(parking_checking_window, image=parking_checking_window_bg_image)
    parking_checking_window_bg_label.place(relwidth=1, relheight=1)

    # Create a new frame for the buttons
    button_frame = tk.Frame(parking_checking_window, bg='black', bd=10)
    button_frame.place(relx=0.5, rely=0.6, anchor='center')  # Adjust the rely parameter to move the frame down

    # Create a button to handle data of users
    Data_button = tk.Button(parking_checking_window, text="Sign Up Information of Students",  width=30, height=2, font=('Times New Roman', 18), command=display_users_table)
    Data_button.pack(pady=20)

    


    # Create a button to handle data of users
    Reservation_button = tk.Button(parking_checking_window, text="Reservation Information",  width=25, height=2, font=('Times New Roman', 18), command=display_reservation_table)
    Reservation_button.pack(pady=20)
 
    

    # Create a button to handle fci layout
    Show_fci_button = tk.Button(parking_checking_window, text="FCI Parking Layout",  width=20, height=2, font=('Times New Roman', 18), command=fci_layout)
    Show_fci_button.pack(pady=20)

    

    # Create a button to handle fcoe layout
    Show_foe_button = tk.Button(parking_checking_window, text="FOE Parking Layout",  width=20, height=2, font=('Times New Roman', 18), command=foe_layout)
    Show_foe_button.pack(pady=20)

    

# Buttons for Sign Up, Student, and Guard 

button_sign_up = tk.Button(root, text="SIGN UP", **button_info, command=button_sign_up)
button_sign_up.pack(pady=20)

button_student = tk.Button(root, text="STUDENT", **button_info, command=student_login)
button_student.pack(pady=20)

button_guard = tk.Button(root, text="GUARD", command=guard_login, **button_info)
button_guard.pack(pady=20)


guide_window = None
student_guide_window = None
signup_window = None

def guide():
    global guide_window
    guide_window = tk.Toplevel(root)
    guide_window.title("Instruction for students and guards")
    guide_window.geometry('900x900')

    image_folder = os.path.join(os.path.dirname(__file__), 'images')
    guide_window_bg_image = tk.PhotoImage(file=os.path.join(image_folder, 'IMAGE 2.png'))
    guide_window.bg_image = guide_window_bg_image
    guide_window_bg_label = tk.Label(guide_window, image=guide_window_bg_image)
    guide_window_bg_label.place(relwidth=1, relheight=1)

    guideselection_frame = tk.Frame(guide_window, bg='white', bd=10)
    guideselection_frame.place(relx=0.5, rely=0.4, anchor='center')  

    label = tk.Label(guideselection_frame, text="ARE YOU A STUDENT OR A GUARD ?", fg='black', bg='white', font=("Times New Roman", 16))
    label.grid(row=0, column=0, padx=10, pady=5)

    button_frame = tk.Frame(guide_window, bg='black', bd=10)
    button_frame.place(relx=0.5, rely=0.6, anchor='center')  

    button_user1 = tk.Button(button_frame, text="STUDENT", font=("Times New Roman", 18), command=student_guide)
    button_user1.grid(row=0, column=0, padx=10, pady=10)

    button_user2 = tk.Button(button_frame, text="GUARD", font=("Times New Roman", 18), command=guard_guide)
    button_user2.grid(row=0, column=1, padx=10, pady=10)


    def go_back():
        guide_window.destroy()  # Destroy the guide selection frame
        signup_window.deiconify()  # Show the signup window again

    back_button = tk.Button(guide_window, text="Back", command=go_back)
    back_button.pack(side=tk.BOTTOM)
    
def student_guide():
    global guide_window, student_guide_window
    guide_window.withdraw()  # Hide the guide window
    student_guide_window = tk.Toplevel(root)
    student_guide_window.title("Instruction for students")
    student_guide_window.geometry('900x900')

    image_folder = os.path.join(os.path.dirname(__file__), 'images')
    student_guide_window_bg_image = tk.PhotoImage(file=os.path.join(image_folder, 'IMAGE 3.png'))
    student_guide_window.bg_image = student_guide_window_bg_image
    student_guide_window_bg_label = tk.Label(student_guide_window, image=student_guide_window_bg_image)
    student_guide_window_bg_label.place(relwidth=1, relheight=1)

    def go_back():
        student_guide_window.destroy()  # Destroy the student_guide_window
        guide_window.deiconify()  # Show the guide window again

    back_button = tk.Button(student_guide_window, text="Back", command=go_back)
    back_button.pack(side=tk.BOTTOM)


def guard_guide():
    global guide_window, guard_guide_window
    guide_window.withdraw()  # Hide the guide window
    guard_guide_window = tk.Toplevel(root)
    guard_guide_window.title("Instruction for guards")
    guard_guide_window.geometry('900x900')

    image_folder = os.path.join(os.path.dirname(__file__), 'images')
    guard_guide_window_bg_image = tk.PhotoImage(file=os.path.join(image_folder, 'IMAGE 4.png'))
    guard_guide_window.bg_image = guard_guide_window_bg_image
    guard_guide_window_bg_label = tk.Label(guard_guide_window, image=guard_guide_window_bg_image)
    guard_guide_window_bg_label.place(relwidth=1, relheight=1)

    def go_back():
        guard_guide_window.destroy()  # Destroy the guard_guide_window
        guide_window.deiconify()  # Show the guide window again

    back_button = tk.Button(guard_guide_window, text="Back", command=go_back)
    back_button.pack(side=tk.BOTTOM)

button_guide = tk.Button(root, text="INSTRUCTION", command=guide, **button_info)
button_guide.pack(pady=20)

# Main loop to run the Tkinter application
root.mainloop()