import os
import json
from datetime import datetime, timedelta
import getpass


class ApplicationTracker:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.applications = []
        self.load_users()
        self.load_data()

    def register_user(self):
        username = input("Create a username: ")
        if username in self.users:
            print("Username already exists. Try again.")
            return
        password = getpass.getpass("Create a password: ")
        self.users[username] = {"password": password, "theme": "light"}
        self.save_users()
        print("Registration successful!")

    def login_user(self):
        username = input("Enter username: ")
        if username not in self.users:
            print("Username does not exist. Please register.")
            return False
        password = getpass.getpass("Enter password: ")
        if self.users[username]["password"] == password:
            self.current_user = username
            print("Login successful!")
            self.load_data()
            return True
        else:
            print("Incorrect password.")
            return False

    def change_password(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        old_password = getpass.getpass("Enter your current password: ")
        if self.users[self.current_user]["password"] != old_password:
            print("Incorrect password.")
            return
        new_password = getpass.getpass("Enter a new password: ")
        self.users[self.current_user]["password"] = new_password
        self.save_users()
        print("Password updated successfully!")

    def set_theme(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        theme = input("Enter theme (light/dark): ").strip().lower()
        if theme not in ["light", "dark"]:
            print("Invalid theme. Try again.")
            return
        self.users[self.current_user]["theme"] = theme
        self.save_users()
        print(f"Theme updated to {theme} mode.")

    def add_application(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        name = input("College Name: ")
        platform = input("Platform: ")
        try:
            deadline = input("Deadline (YYYY-MM-DD): ")
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return
        essay_prompt = input("Essay Prompt: ")
        app = {
            "name": name,
            "platform": platform,
            "deadline": deadline,
            "essay_prompt": essay_prompt,
            "status": "Not Started",
            "notes": ""
        }
        self.applications.append(app)
        self.save_data()

    def suggest_dates(self):
        if not self.current_user:
            print("You need to log in first.")
            return
        for app in self.applications:
            deadline = datetime.strptime(app["deadline"], "%Y-%m-%d")
            suggested_start = deadline - timedelta(days=14)
            print(f"Start working on {app['name']} on {suggested_start.date()}")

    def save_data(self):
        if not self.current_user:
            return
        filename = f"{self.current_user}_applications.json"
        with open(filename, "w") as file:
            json.dump(self.applications, file)

    def load_data(self):
        if not self.current_user:
            return
        filename = f"{self.current_user}_applications.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.applications = json.load(file)

    def save_users(self):
        with open("users.json", "w") as file:
            json.dump(self.users, file)

    def load_users(self):
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                self.users = json.load(file)


if __name__ == "__main__":
    tracker = ApplicationTracker()
    while True:
        print("\nCollege Application Tracker")
        print("1. Register")
        print("2. Login")
        print("3. Add Application")
        print("4. Suggest Dates")
        print("5. Change Password")
        print("6. Set Theme")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            tracker.register_user()
        elif choice == "2":
            tracker.login_user()
        elif choice == "3":
            tracker.add_application()
        elif choice == "4":
            tracker.suggest_dates()
        elif choice == "5":
            tracker.change_password()
        elif choice == "6":
            tracker.set_theme()
        elif choice == "7":
            break
        else:
            print("Invalid choice, please try again.")
