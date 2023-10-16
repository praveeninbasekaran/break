import re

class RegistrationLogic:
    def __init__(self):
        pass

    def is_valid_password(self, password):
        # Password strength criteria: 1 capital letter, 1 small letter, 1 numeric, and 1 special character
        if re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])', password):
            return True
        else:
            return False

    def register_user(self, user_data):
        first_name = user_data["first_name"]
        last_name = user_data["last_name"]
        email = user_data["email"]
        phone = user_data["phone"]
        password = user_data["password"]

        # Check password strength
        if not self.is_valid_password(password):
            print("Password does not meet the criteria")
            return

        # Perform the registration process (store user data, etc.)
        # ...
