import json
from datetime import datetime

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Function to display menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. View Tasks")
    print("5. Exit")

# Function to add a task
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter task priority (high/medium/low): ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    tasks.append({
        "name": task_name,
        "priority": priority,
        "due_date": due_date.strftime("%Y-%m-%d"),
        "completed": False
    })
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']} - Due: {task['due_date']} - Priority: {task['priority']}")

    choice = int(input("Enter task number to remove: "))
    if 1 <= choice <= len(tasks):
        del tasks[choice - 1]
        print("Task removed successfully.")
    else:
        print("Invalid task number.")

# Function to mark a task as completed
def mark_completed(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']} - Due: {task['due_date']} - Priority: {task['priority']}")

    choice = int(input("Enter task number to mark as completed: "))
    if 1 <= choice <= len(tasks):
        tasks[choice - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index}. {task['name']} - Due: {task['due_date']} - Priority: {task['priority']} - {status}")

# Main function
def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            view_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
