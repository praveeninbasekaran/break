import tkinter as tk
import csv
from hashlib import sha256

class RegistrationGUI:
    def __init__(self, parent_frame, close_callback):
        self.parent_frame = parent_frame
        self.close_callback = close_callback

        # Create labels and entry fields for registration details
        self.create_registration_form()

        # Create a "Register" button
        register_button = tk.Button(self.parent_frame, text="Register", command=self.register)
        register_button.pack()

    def create_registration_form(self):
        # Create labels and entry fields for registration details
        self.first_name_label = tk.Label(self.parent_frame, text="First Name:")
        self.first_name_entry = tk.Entry(self.parent_frame)
        self.last_name_label = tk.Label(self.parent_frame, text="Last Name:")
        self.last_name_entry = tk.Entry(self.parent_frame)
        self.phone_label = tk.Label(self.parent_frame, text="Phone:")
        self.phone_entry = tk.Entry(self.parent_frame)
        self.email_label = tk.Label(self.parent_frame, text="Email:")
        self.email_entry = tk.Entry(self.parent_frame)
        self.password_label = tk.Label(self.parent_frame, text="Password:")
        self.password_entry = tk.Entry(self.parent_frame, show="*")

        # Pack labels and entry fields
        self.first_name_label.pack()
        self.first_name_entry.pack()
        self.last_name_label.pack()
        self.last_name_entry.pack()
        self.phone_label.pack()
        self.phone_entry.pack()
        self.email_label.pack()
        self.email_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()

    def register(self):
        # Get user data from entry fields
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Hash the password
        password_hash = self.hash_password(password)

        # Create a dictionary to represent the user data
        user_data = {
            "First Name": first_name,
            "Last Name": last_name,
            "Phone": phone,
            "Email": email,
            "Password": password_hash,
        }

        # Define the CSV file name
        csv_file = "user_data.csv"

        # Write user data to the CSV file
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=user_data.keys())
            # Check if the CSV file is empty, and if so, write the header row
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(user_data)

        # Inform the user that registration is successful (you can customize this part)
        print("Registration successful!")

        # Close the registration form
        self.close_callback()

    def hash_password(self, password):
        # Generate a random salt (you can modify this)
        salt = "somesalt"

        # Combine the password and salt and then hash it
        password_hash = sha256((password + salt).encode()).hexdigest()
        return password_hash
