# Task 1 – To-Do List

## CODSOFT Python Programming Internship

### Overview
A command-line To-Do List application that helps users manage and organize their daily tasks. Users can add, view, update, complete, and delete tasks. All tasks are saved to a file so they persist between runs.

### Features
- **Add Task** – Add a new task to your list.
- **View Tasks** – See all tasks with their completion status.
- **Update Task** – Edit the description of an existing task.
- **Mark as Done** – Mark a task as completed.
- **Delete Task** – Remove a task from the list.
- **Persistent Storage** – Tasks are saved to `tasks.txt` so nothing is lost when you close the program.

### How to Run
```bash
python3 task1_todo_list.py
```

### Sample Usage
```
===== TO-DO LIST =====
1. View Tasks
2. Add Task
3. Update Task
4. Mark Task as Done
5. Delete Task
6. Exit
Choose an option (1-6): 2
Enter the new task: Finish Python assignment
Task added successfully!
```

### Tech Used
- Python 3 (standard library only — no external packages required)
- File I/O for persistent storage

### Possible Improvements
- Add due dates and priority levels
- Build a GUI version using Tkinter
- Add sorting/filtering options (e.g., show only pending tasks)

---
*Part of the CODSOFT Python Programming Internship – [www.codsoft.in](https://www.codsoft.in)*

