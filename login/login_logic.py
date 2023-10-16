import csv
from hashlib import sha256

class LoginLogic:
    def authenticate(self, email, password):
        # Load user data from the CSV file (user_data.csv)
        user_data = self.load_user_data()

        # Hash the provided password
        password_hash = self.hash_password(password)

        # Check if the user with the provided email and password exists
        for user in user_data:
            if user["Email"] == email and user["Password"] == password_hash:
                return True

        return False

    def load_user_data(self):
        user_data = []
        csv_file = "user_data.csv"

        with open(csv_file, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_data.append(row)

        return user_data

    def hash_password(self, password):
        # Generate a random salt (you can modify this)
        salt = "somesalt"

        # Combine the password and salt and then hash it
        password_hash = sha256((password + salt).encode()).hexdigest()
        return password_hash
