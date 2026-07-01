"""
CODSOFT Python Programming Internship
Task 1 - To-Do List Application

A simple command-line To-Do List app that lets the user:
- Add tasks
- View all tasks
- Update/edit a task
- Mark a task as done
- Delete a task

Tasks are saved to a text file (tasks.txt) so they persist between runs.
"""

import os

TASKS_FILE = "tasks.txt"


def load_tasks():
    """Read tasks from the file and return them as a list of dicts."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                status, description = line.split("|", 1)
                tasks.append({"done": status == "1", "description": description})
    return tasks


def save_tasks(tasks):
    """Write the current list of tasks back to the file."""
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            status = "1" if task["done"] else "0"
            f.write(f"{status}|{task['description']}\n")


def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")


def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "[X]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['description']}")


def add_task(tasks):
    description = input("Enter the new task: ").strip()
    if description:
        tasks.append({"done": False, "description": description})
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task description cannot be empty.")


def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_description = input("Enter the new task description: ").strip()
            if new_description:
                tasks[index]["description"] = new_description
                save_tasks(tasks)
                print("Task updated successfully!")
            else:
                print("Task description cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def mark_task_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted task: {removed['description']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_task_done(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
