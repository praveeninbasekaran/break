import tkinter as tk
from tkinter import ttk

class LoginGUI:
    def __init__(self, root, authenticate_callback, show_registration_callback):
        self.root = root
        self.authenticate_callback = authenticate_callback
        self.show_registration_callback = show_registration_callback
        self.create_login_ui()

    def create_login_ui(self):
        # Set the root window's background to white
        self.root.configure(bg="white")

        # Create a custom style
        style = ttk.Style()
        style.configure('TFrame', background='white')
        style.configure('TLabel', background='white', font=('Helvetica', 12))
        style.configure('TButton', background='white', font=('Helvetica', 12))
        style.map('TButton', background=[('active', 'white')])

        # Create a login frame with a white background
        login_frame = ttk.Frame(self.root, style='TFrame')
        login_frame.grid(row=0, column=0, padx=10, pady=10)

        # Create login labels and entry fields
        ttk.Label(login_frame, text="Email:").grid(row=0, column=0, pady=5)
        self.email_entry = ttk.Entry(login_frame)
        self.email_entry.grid(row=0, column=1, pady=5)

        ttk.Label(login_frame, text="Password:").grid(row=1, column=0, pady=5)
        self.password_entry = ttk.Entry(login_frame, show="*")  # Show asterisks for password
        self.password_entry.grid(row=1, column=1, pady=5)

        # Create login and new user buttons with custom style
        login_button = ttk.Button(login_frame, text="Login", command=self.authenticate_callback, style='TButton')
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        new_user_button = ttk.Button(login_frame, text="New User", command=self.show_registration_callback, style='TButton')
        new_user_button.grid(row=3, column=0, columnspan=2, pady=10)


    def login(self):
        # Get user login data from entry fields
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Call the authenticate_callback with email and password
        if self.authenticate_callback(email, password):
            # Login successful, you can handle this part (e.g., show a welcome message)
            print("Login successful!")
        else:
            # Login failed, you can handle this part (e.g., show an error message)
            print("Login failed!")