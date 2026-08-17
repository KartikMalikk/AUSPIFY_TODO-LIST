"""
=========================================
        TO-DO LIST APPLICATION
=========================================

Features:
✔ Add Tasks
✔ View Tasks
✔ Mark Tasks as Completed
✔ Delete Tasks
✔ Save Tasks Automatically
✔ Load Tasks on Startup
"""

import os

FILE_NAME = "tasks.txt"


# ----------------------------------------
# Load Tasks
# ----------------------------------------
def load_tasks():
    tasks = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    status, task = line.split("|", 1)

                    tasks.append({
                        "task": task,
                        "completed": status == "Done"
                    })

    return tasks


# ----------------------------------------
# Save Tasks
# ----------------------------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:

            status = "Done" if task["completed"] else "Pending"

            file.write(f"{status}|{task['task']}\n")


# ----------------------------------------
# Display Tasks
# ----------------------------------------
def view_tasks(tasks):

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== TASK LIST ==========")

    for index, task in enumerate(tasks, start=1):

        symbol = "✅" if task["completed"] else "❌"

        print(f"{index}. {symbol} {task['task']}")

    print("===============================\n")


# ----------------------------------------
# Add Task
# ----------------------------------------
def add_task(tasks):

    task = input("Enter new task: ").strip()

    if task == "":
        print("Task cannot be empty.")
        return

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks(tasks)

    print("Task added successfully!")


# ----------------------------------------
# Mark Task Completed
# ----------------------------------------
def complete_task(tasks):

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):

            tasks[number - 1]["completed"] = True

            save_tasks(tasks)

            print("Task marked as completed!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# ----------------------------------------
# Delete Task
# ----------------------------------------
def delete_task(tasks):

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):

            deleted = tasks.pop(number - 1)

            save_tasks(tasks)

            print(f"Deleted: {deleted['task']}")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# ----------------------------------------
# Main Program
# ----------------------------------------
tasks = load_tasks()

while True:

    print("""
=====================================
        TO-DO LIST MENU
=====================================

1. Add Task

2. View Tasks

3. Mark Task Completed

4. Delete Task

5. Exit

=====================================
""")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        complete_task(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        save_tasks(tasks)
        print("\nTasks saved successfully!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")