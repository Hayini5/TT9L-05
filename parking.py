import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('parking_system.db')

# Create a cursor object
c = conn.cursor()

# Create a table for users
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        user_id TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        vehicle_type TEXT,
        vehicle_number TEXT,
        gender_type TEXT NOT NULL,
        faculty TEXT
    )
''')

# Add the vehicle_type column to the users table
try:
    c.execute('ALTER TABLE users ADD COLUMN vehicle_type TEXT')
    print("Column 'vehicle_type' added successfully.")
except sqlite3.OperationalError as e:
    print("Error:", e)

# Commit the changes and close the connection
conn.commit()
conn.close()

# Function to validate MMU student ID
def validate_mmu_id(student_id):
    return student_id.startswith("MMU") and len(student_id) == 10 and student_id[3:].isdigit()

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

# Function to handle the sign-up process
def button_sign_up():
    # Create a new top-level window for sign up form
    signup_window = tk.Toplevel(root)
    signup_window.title("SIGN UP FORM")
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

    # Vehicle Type Label and OptionMenu
    label_vehicle_type = tk.Label(signupform_frame, text="Vehicle Type", fg='black', bg='white')
    label_vehicle_type.grid(row=3, column=0, padx=10, pady=5)

    vehicle_type = tk.StringVar(signupform_frame)
    vehicle_type.set("Select")  # default value
    option_vehicle_type = tk.OptionMenu(signupform_frame, vehicle_type, "Car", "Motor")
    option_vehicle_type.grid(row=3, column=1, padx=10, pady=5)

    # Vehicle Number Plate Label and Entry
    label_vehicle_number = tk.Label(signupform_frame, text="Vehicle Number Plate", fg='black', bg='white')
    label_vehicle_number.grid(row=4, column=0, padx=10, pady=5)

    entry_vehicle_number = tk.Entry(signupform_frame)
    entry_vehicle_number.grid(row=4, column=1, padx=10, pady=5)

    # Gender and OptionMenu
    gender_type_label = tk.Label(signupform_frame, text="Gender", fg='black', bg='white')
    gender_type_label.grid(row=5, column=0, padx=10, pady=5)

    gender_type = tk.StringVar(signupform_frame)
    gender_type.set("Select")  # default value
    option_gender_type = tk.OptionMenu(signupform_frame, gender_type, "Female", "Male")
    option_gender_type.grid(row=5, column=1, padx=10, pady=5)

    # Function to handle submission
    def submit():
        name = entry_name.get()
        user_id = entry_id.get()
        password = entry_password.get()
        v_type = vehicle_type.get()
        v_number = entry_vehicle_number.get()
        g_type = gender_type.get()

        if not name or not user_id or not password or not v_number or not v_type or not g_type:
            messagebox.showwarning("Input Error", "All fields are required.")
        else:
            # Insert user data into the SQLite database
            try:
                conn = sqlite3.connect('parking_system.db')
                c = conn.cursor()
                c.execute('''
                    INSERT INTO users (name, user_id, password, vehicle_type, vehicle_number, gender_type) VALUES (?, ?, ?, ?, ?, ?)
                ''', (name, user_id, password, v_type, v_number, g_type))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sign Up", "Sign Up Successful!")
                signup_window.destroy()
            except sqlite3.IntegrityError:
                 messagebox.showerror("Error", "User ID already exists. Please choose a different one.")
            except Exception as e:
                 messagebox.showerror("Error", str(e))

    # Submit Button
    button_submit = tk.Button(signupform_frame, text="SIGN UP", command=submit)
    button_submit.grid(row=6, column=1, padx=10, pady=10)

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

    # Gender and OptionMenu
    gender_type_label = tk.Label(signupform_frame, text="Gender",  fg='black', bg='white')
    gender_type_label.grid(row=3, column=0, padx=10, pady=5)

    gender_type = tk.StringVar(signupform_frame)
    gender_type.set("select")  # default value
    option_gender_type = tk.OptionMenu(signupform_frame, gender_type, "Female", "Male")
    option_gender_type.grid(row=3, column=1, padx=10, pady=5)

    def toggle_password():
        if entry_password.cget('show')== '':
            entry_password.config(show='*')
            toggle_button.config(text='show')
        else:
            entry_password.config(show='')
            toggle_button.config(text='hide')
        
    toggle_button = tk.Button(signupform_frame, text='Show', command=toggle_password)
    toggle_button.grid(row=2, column=2, padx=10, pady=5)

     # Faculty and Entry
    faculty_label = tk.Label(signupform_frame, text="Faculty", fg='black', bg='white')
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
        else:
            # Insert user data into the SQLite database
            try:
                conn = sqlite3.connect('parking_system.db')
                c = conn.cursor()
                c.execute('''
                    INSERT INTO users (name, user_id, password, gender_type, faculty) VALUES (?, ?, ?, ?, ?)
                ''', (name, guard_id, password, g_type, faculty))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sign Up", "Sign Up Successful!")
                signup_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Sign Up Error", "Guard ID already exists. Please choose a different one.")
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

    # Submit Button
    button_submit = tk.Button(signupform_frame, text="Submit", command=submit)
    button_submit.grid(row=5, column=1, padx=10, pady=10)


# Function to handle the student login process
def student_login():
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
            conn = sqlite3.connect('parking_system.db')
            c = conn.cursor()
            c.execute('''
                SELECT * FROM users WHERE user_id = ? AND password = ?
            ''', (student_id, password))
            result = c.fetchone()
            conn.close()
            if result:
                messagebox.showinfo("Login", "Login Successful!")
                student_window.destroy()
                # Call parking_system function after displaying user information
                parking_system()
            else:
                messagebox.showerror("Login Error", "Invalid User ID or Password")

    # Forget Password Button
    button_forget = tk.Button(loginform_frame, text="Forget Password", font=("Microsoft YaHei UI Light", 8, 'bold'), fg='red', command=submit)
    button_forget.grid(row=3, column=1, sticky="e", pady=5, padx=10)

    # Submit Button
    button_submit = tk.Button(loginform_frame, text="LOGIN", font=("Microsoft YaHei UI Light", 16), fg='black', command=submit)
    button_submit.grid(row=4, columnspan=2, pady=10)

    # Function to handle the booking, cancelation and extension
def parking_system():
    # Create a new top-level window for parking system
    parking_system_window = tk.Toplevel(root)
    parking_system_window.title("Parking Confirmation")
    parking_system_window.geometry('900x900')

    parking_system_bg_image = tk.PhotoImage(file=r"C:\Users\KARTHIGHAYINI\Downloads\road-highway.png")
    parking_system_window.bg_image = parking_system_bg_image  # keep a reference to avoid garbage collection
    parking_system_bg_label = tk.Label(parking_system_window, image=parking_system_bg_image)
    parking_system_bg_label.place(relwidth=1, relheight=1)

    # Create a new frame for the buttons
    button_frame = tk.Frame(parking_system_window, bg='black', bd=10)
    button_frame.place(relx=0.5, rely=0.6, anchor='center')  # Adjust the rely parameter to move the frame down

    # Create a button to handle booking
    book_button = tk.Button(parking_system_window, text="Book",  width=20, height=2, font=('Times New Roman', 18), command=open_booking_window)
    book_button.pack(pady=20)

    # Create a button to handle cancellation
    cancel_button = tk.Button(parking_system_window, text="Cancel",  width=20, height=2, font=('Times New Roman', 18), command=parking_system)
    cancel_button.pack(pady=20)

    # Create a button to handle extension
    extend_button = tk.Button(parking_system_window, text="Extend",  width=20, height=2, font=('Times New Roman', 18), command=parking_system)
    extend_button.pack(pady=20)

    # Fuction to handle the booking process
def open_booking_window():
    # Create a new top-level-window for book form
    book_window = tk.Toplevel(root)
    book_window.title("BOOKING")
    book_window.geometry('900x900')

    book_bg_image = tk.PhotoImage(file=r"C:\Users\KARTHIGHAYINI\Downloads\road-highway.png")
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

    # Function to let student choose parking space
    # Function to let student choose parking space
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

    # Function to handle button clicks
    def reserve_space(space):
        # Create a new window for time selection
        time_selection_window= tk.Toplevel(space_selection_window)
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

        # Fuction to confirm reservation with selected time
        def confirm_reservation():
            chosen_start_time = start_time.get()
            chosen_end_time = end_time.get()
            messagebox.showinfo("Parking Space", f"Parking Space {space} reserved successfull from {chosen_start_time} to {chosen_end_time}!")
            button_dict[space].config(bg='red') #change button colour to red
            time_selection_window.destroy()

        # Confirm button
        confirm_button = tk.Button(time_selection_window, text="RESERVED",bg='green', font=("Microsoft YaHei UI Light", 10), fg='white', command=confirm_reservation)
        confirm_button.grid(row=2, columnspan=2, pady=20)

    # Create buttons for each parking space
    for i in range(1, 51):
        button_text = f"Space {i}"
        button = tk.Button(layout_frame, text=f"Space {i}", font=("Arial", 10), width=10, height=2,
                           command=lambda i=i: reserve_space(i))
        row = (i - 1) // 10
        col = (i - 1) % 10
        button.grid(row=row, column=col, padx=5, pady=5)
        button_dict[i] = button #Store button reference in dictionary

    # Function to let student choose parking space
    # Function to let student choose parking space
def foe_layout():
    # Create a new top-level window for parking space selection
    space_selection_window = tk.Toplevel(root)
    space_selection_window.title('Choose Parking Space')
    space_selection_window.geometry('900x900')

    # Create a frame to hold the parking layout
    layout_frame = tk.Frame(space_selection_window, bg='white', bd=10)
    layout_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Function to handle button clicks
    def reserve_space(space):
        messagebox.showinfo("Parking Space", f"Parking Space {space} reserved successfully!")

        # Here, you can add code to update the database with the selected parking space
        # For example, you can insert a record into the vehicles table with the user_id and selected parking space

    # Create buttons for each parking space
    for i in range(1, 51):
        button_text = f"Space {i}"
        button = tk.Button(layout_frame, text=button_text, font=("Arial", 10), width=10, height=2,
                           command=lambda i=i: reserve_space(i))
        row = (i - 1) // 10
        col = (i - 1) % 10
        button.grid(row=row, column=col, padx=5, pady=5)
        
    # Function to handle the guard login process
def guard_login():
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

# Buttons for Sign Up, Student, and Guard 

button_sign_up = tk.Button(root, text="SIGN UP", **button_info, command=button_sign_up)
button_sign_up.pack(pady=20)

button_student = tk.Button(root, text="STUDENT", width=20, height=2, font=('Times New Roman', 18), command=student_login)
button_student.pack(pady=20)

button_guard = tk.Button(root, text="GUARD", command=guard_login, **button_info)
button_guard.pack(pady=20)

# Main loop to run the Tkinter application
root.mainloop()