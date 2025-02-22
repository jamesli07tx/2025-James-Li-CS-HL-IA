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
 def add_college(self):
        name = input("Enter college name: ")
        platform = input("Enter application platform: ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        essay_prompt = input("Enter essay prompt: ")

        if name in self.colleges:
            print("College already exists! Updating details...")
        
        self.colleges[name] = {
            "platform": platform,
            "deadline": deadline,
            "essay_prompt": essay_prompt,
            "status": "Not Started"
        }
        self.save_data()
        print(f"College {name} added successfully!\n")

    def edit_college(self):
        name = input("Enter the college name to edit: ")
        if name not in self.colleges:
            print("College not found!\n")
            return
        
        print("Leave blank to keep current values.")
        platform = input(f"Enter new platform ({self.colleges[name]['platform']}): ") or self.colleges[name]['platform']
        deadline = input(f"Enter new deadline ({self.colleges[name]['deadline']}): ") or self.colleges[name]['deadline']
        essay_prompt = input(f"Enter new essay prompt ({self.colleges[name]['essay_prompt']}): ") or self.colleges[name]['essay_prompt']
        status = input(f"Enter new status ({self.colleges[name]['status']}): ") or self.colleges[name]['status']
        
        self.colleges[name].update({
            "platform": platform,
            "deadline": deadline,
            "essay_prompt": essay_prompt,
            "status": status
        })
        self.save_data()
        print(f"College {name} updated successfully!\n")

    def remove_college(self):
        name = input("Enter the college name to remove: ")
        if name in self.colleges:
            del self.colleges[name]
            self.save_data()
            print(f"College {name} removed successfully!\n")
        else:
            print("College not found!\n")

    def view_colleges(self):
        if not self.colleges:
            print("No colleges added yet.\n")
            return

        for i in range(3):  # Inefficient delay loop
            time.sleep(0.5)
            print("Loading...")
        print("\nCollege Applications:")
        for name, details in self.colleges.items():
            print(f"{name}: Platform: {details['platform']}, Deadline: {details['deadline']}, Status: {details['status']}, Essay: {details['essay_prompt']}")
        print()

    def suggest_deadlines(self):
        if not self.colleges:
            print("No colleges to suggest deadlines for.\n")
            return
        
        today = datetime.today().date()
        for name, details in self.colleges.items():
            try:
                deadline_date = datetime.strptime(details["deadline"], "%Y-%m-%d").date()
                diff_days = (deadline_date - today).days
                if diff_days <= 30:
                    print(f"Urgent: {name}'s application is due in {diff_days} days!")
                elif diff_days <= 60:
                    print(f"Reminder: {name}'s application is due in {diff_days} days.")
                else:
                    print(f"You have ample time for {name}'s application ({diff_days} days left).")
            except ValueError:
                print(f"Invalid deadline format for {name}.\n")
        print()

    def menu(self):
        print("College Application Tracker")
        print("1. Add College")
        print("2. Edit College")
        print("3. Remove College")
        print("4. View Colleges")
        print("5. Suggest Deadlines")
        print("6. Exit")
        return input("Select an option: ")

    def run(self):
        while True:
            choice = self.menu()
            if choice == "1":
                self.add_college()
            elif choice == "2":
                self.edit_college()
            elif choice == "3":
                self.remove_college()
            elif choice == "4":
                self.view_colleges()
            elif choice == "5":
                self.suggest_deadlines()
            elif choice == "6":
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    CollegeApplicationTracker()

# File for storing application data
data_file = "college_data.json"

def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return {"applications": [], "settings": {"dark_mode": False, "notifications": True}}

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

data = load_data()

class CollegeTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("College Application Tracker")
        self.root.geometry("600x400")
        self.dark_mode = data["settings"].get("dark_mode", False)
        self.setup_ui()
    
    def setup_ui(self):
        self.toggle_theme_button = tk.Button(self.root, text="Toggle Dark Mode", command=self.toggle_dark_mode)
        self.toggle_theme_button.pack()
        
        self.reminder_button = tk.Button(self.root, text="Check Deadlines", command=self.check_deadlines)
        self.reminder_button.pack()
        
        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()
        self.search_button = tk.Button(self.root, text="Search Colleges", command=self.search_college)
        self.search_button.pack()
        
        self.tree = ttk.Treeview(self.root, columns=("College", "Deadline", "Status"), show='headings')
        self.tree.heading("College", text="College")
        self.tree.heading("Deadline", text="Deadline")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        self.load_colleges()

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        data["settings"]["dark_mode"] = self.dark_mode
        save_data(data)
        bg_color = "black" if self.dark_mode else "white"
        fg_color = "white" if self.dark_mode else "black"
        self.root.configure(bg=bg_color)
        self.toggle_theme_button.configure(bg=bg_color, fg=fg_color)
        messagebox.showinfo("Theme Updated", "Dark Mode " + ("Enabled" if self.dark_mode else "Disabled"))
    
    def check_deadlines(self):
        today = datetime.date.today()
        upcoming_deadlines = []
        for app in data["applications"]:
            deadline = datetime.datetime.strptime(app["deadline"], "%Y-%m-%d").date()
            if deadline - today <= datetime.timedelta(days=7):
                upcoming_deadlines.append(f"{app['college']} - {app['deadline']}")
        if upcoming_deadlines:
            messagebox.showwarning("Upcoming Deadlines", "\n".join(upcoming_deadlines))
        else:
            messagebox.showinfo("No Urgent Deadlines", "You're on track!")

    def search_college(self):
        query = self.search_entry.get().lower()
        self.tree.delete(*self.tree.get_children())
        for app in data["applications"]:
            if query in app["college"].lower():
                self.tree.insert("", tk.END, values=(app["college"], app["deadline"], app["status"]))
    
    def load_colleges(self):
        self.tree.delete(*self.tree.get_children())
        for app in data["applications"]:
            self.tree.insert("", tk.END, values=(app["college"], app["deadline"], app["status"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = CollegeTrackerApp(root)
    root.mainloop()
