import pickle
from datetime import datetime

class Project:
    def __init__(self, name, start_date, completion_percentage, priority):
        self.name = name
        self.start_date = start_date
        self.completion_percentage = completion_percentage
        self.priority = priority

    def display(self):
        print(f"{self.name} - Start Date: {self.start_date}, Completion: {self.completion_percentage}%, Priority: {self.priority}")

    def is_completed(self):
        return self.completion_percentage == 100

    def is_started_after(self, date):
        return self.start_date > date

    def update(self, completion_percentage=None, priority=None):
        if completion_percentage is not None:
            self.completion_percentage = completion_percentage
        if priority is not None:
            self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

def load_projects(filename):
    try:
        with open(filename, 'rb') as file:
            projects = pickle.load(file)
        return projects
    except FileNotFoundError:
        return []

def save_projects(filename, projects):
    with open(filename, 'wb') as file:
        pickle.dump(projects, file)

def display_projects(projects):
    incomplete_projects = [p for p in projects if not p.is_completed()]
    completed_projects = [p for p in projects if p.is_completed()]

    print("\nIncomplete Projects:")
    for project in sorted(incomplete_projects):
        project.display()

    print("\nCompleted Projects:")
    for project in sorted(completed_projects):
        project.display()

def filter_projects_by_date(projects, filter_date):
    filtered_projects = [p for p in projects if p.is_started_after(filter_date)]
    print("\nFiltered Projects:")
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        project.display()

def add_new_project(projects):
    name = input("Enter project name: ")
    start_date = datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
    completion_percentage = int(input("Enter completion percentage: "))
    priority = int(input("Enter priority: "))

    new_project = Project(name, start_date, completion_percentage, priority)
    projects.append(new_project)
    print("New project added successfully!")

def update_project(projects):
    project_index = int(input("Enter the index of the project to update: "))
    if 0 <= project_index < len(projects):
        completion_percentage = input("Enter new completion percentage (leave blank to retain existing value): ")
        priority = input("Enter new priority (leave blank to retain existing value): ")

        projects[project_index].update(
            completion_percentage=int(completion_percentage) if completion_percentage else None,
            priority=int(priority) if priority else None
        )

        print("Project updated successfully!")
    else:
        print("Invalid project index.")

def main():
    projects_filename = "projects_data.pkl"
    projects = load_projects(projects_filename)

    while True:
        print("\nProject Management Menu:")
        print("1. Load projects")
        print("2. Save projects")
        print("3. Display projects")
        print("4. Filter projects by date")
        print("5. Add new project")
        print("6. Update project")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            filename = input("Enter the filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == '2':
            filename = input("Enter the filename to save projects to: ")
            save_projects(filename, projects)
            print("Projects saved successfully!")
        elif choice == '3':
            display_projects(projects)
        elif choice == '4':
            filter_date = datetime.strptime(input("Enter the filter date (YYYY-MM-DD): "), "%Y-%m-%d")
            filter_projects_by_date(projects, filter_date)
        elif choice == '5':
            add_new_project(projects)
        elif choice == '6':
            update_project(projects)
        elif choice == '7':
            save_projects(projects_filename, projects)
            print("Projects saved. Quitting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
