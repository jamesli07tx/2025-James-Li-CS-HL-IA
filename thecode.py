import os
import json
from datetime import datetime, timedelta

class ApplicationTracker:
    def __init__(self):
        self.applications = []
        self.load_data()

    def add_application(self, name, platform, deadline, essay_prompt):
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

    def edit_application(self, index, name=None, platform=None, deadline=None, essay_prompt=None, status=None, notes=None):
        if 0 <= index < len(self.applications):
            app = self.applications[index]
            app["name"] = name or app["name"]
            app["platform"] = platform or app["platform"]
            app["deadline"] = deadline or app["deadline"]
            app["essay_prompt"] = essay_prompt or app["essay_prompt"]
            app["status"] = status or app["status"]
            app["notes"] = notes or app["notes"]
            self.save_data()

    def list_applications(self):
        for idx, app in enumerate(self.applications):
            print(f"{idx}. {app['name']} ({app['platform']}) - {app['deadline']} - {app['status']}")

    def remove_application(self, index):
        if 0 <= index < len(self.applications):
            self.applications.pop(index)
            self.save_data()

    def search_application(self, keyword):
        results = [app for app in self.applications if keyword.lower() in app["name"].lower()]
        for app in results:
            print(f"{app['name']} ({app['platform']}) - {app['deadline']}")

    def save_data(self):
        with open("applications.json", "w") as file:
            json.dump(self.applications, file)

    def load_data(self):
        if os.path.exists("applications.json"):
            with open("applications.json", "r") as file:
                self.applications = json.load(file)

    def suggest_dates(self):
        for app in self.applications:
            deadline = datetime.strptime(app["deadline"], "%Y-%m-%d")
            suggested_start = deadline - timedelta(days=14)
            print(f"Start working on {app['name']} on {suggested_start.date()}")

if __name__ == "__main__":
    tracker = ApplicationTracker()
    while True:
        print("\nCollege Application Tracker")
        print("1. Add Application")
        print("2. Edit Application")
        print("3. List Applications")
        print("4. Remove Application")
        print("5. Search Application")
        print("6. Suggest Dates")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("College Name: ")
            platform = input("Platform: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            essay_prompt = input("Essay Prompt: ")
            tracker.add_application(name, platform, deadline, essay_prompt)
        elif choice == "2":
            tracker.list_applications()
            idx = int(input("Enter the index of the application to edit: "))
            name = input("New College Name (leave blank to keep unchanged): ")
            platform = input("New Platform (leave blank to keep unchanged): ")
            deadline = input("New Deadline (leave blank to keep unchanged): ")
            essay_prompt = input("New Essay Prompt (leave blank to keep unchanged): ")
            status = input("New Status (leave blank to keep unchanged): ")
            notes = input("New Notes (leave blank to keep unchanged): ")
            tracker.edit_application(idx, name, platform, deadline, essay_prompt, status, notes)
        elif choice == "3":
            tracker.list_applications()
        elif choice == "4":
            tracker.list_applications()
            idx = int(input("Enter the index of the application to remove: "))
            tracker.remove_application(idx)
        elif choice == "5":
            keyword = input("Enter keyword to search for: ")
            tracker.search_application(keyword)
        elif choice == "6":
            tracker.suggest_dates()
        elif choice == "7":
            break
        else:
            print("Invalid choice, please try again.")
#part of the code submission