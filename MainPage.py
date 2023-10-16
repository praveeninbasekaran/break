import tkinter as tk
from login.login_gui import LoginGUI
from login.login_logic import LoginLogic
from registration.registration_gui import RegistrationGUI
from registration.registration_logic import RegistrationLogic

# Create the main application window
root = tk.Tk()
root.title("Login and Registration")
root.attributes('-fullscreen', True)  # Set the main window to full screen

# Initialize login logic object
login_logic = LoginLogic()

# Function to show the login screen
def show_login_screen():
    login_frame.pack()
    registration_frame.pack_forget()

# Function to close the registration page and show the login page
def close_registration_page():
    registration_frame.pack_forget()
    show_login_screen()

# Function to show the registration screen
def show_registration_screen():
    login_frame.pack_forget()
    registration_frame.pack()
    registration_gui = RegistrationGUI(registration_frame, close_registration_page)

# Function to close the application when the close button is clicked
def close_window():
    root.destroy()

# Center login fields both horizontally and vertically
def center_login_fields():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = screen_width // 2
    y = screen_height // 2

    login_frame.place(x=x, y=y)

# Create the login frame
login_frame = tk.Frame(root)
login_frame.pack(fill="both", expand=True)
center_login_fields()  # Center the login fields

login_gui = LoginGUI(login_frame, login_logic.authenticate, show_registration_screen)

# Create the registration frame
registration_frame = tk.Frame(root)
registration_logic = RegistrationLogic()
registration_frame.pack(fill="both", expand=True)
registration_frame.pack_forget()  # Start with the registration frame hidden

# Create a close button (label) in the top-left corner
close_button = tk.Label(root, text="✕", font=("Helvetica", 14))
close_button.place(x=10, y=10)
close_button.bind("<Button-1>", lambda event: close_window())

# Start with the login screen
show_login_screen()

# Start the main event loop
root.mainloop()
