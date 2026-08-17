# To-Do List Application

## 📌 Description

The **To-Do List Application** is a simple Python-based task management program designed to help users organize and manage their daily tasks efficiently.

The application provides a menu-driven interface where users can add new tasks, view existing tasks, mark tasks as completed, and delete unwanted tasks. Task information is automatically saved to a text file so that tasks remain available even after the program is closed.

---

## 🚀 Features

* ✅ Add new tasks
* 📋 View all tasks
* ✔️ Mark tasks as completed
* 🗑️ Delete unwanted tasks
* 💾 Automatically save tasks to a file
* 📂 Load previously saved tasks when the application starts
* 🔄 Persistent task data
* 🛡️ Input validation for invalid entries

---

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* File Handling
* `os` module

---

## 📁 Project Structure

```text
To_Do_List/
│
├── todo.py
├── tasks.txt
├── README.md
└── requirements.txt
```

### File Description

| File               | Purpose                        |
| ------------------ | ------------------------------ |
| `todo.py`          | Main Python application        |
| `tasks.txt`        | Stores task data               |
| `README.md`        | Project documentation          |
| `requirements.txt` | Project dependency information |

---

## ⚙️ How the Application Works

### 1. Add Task

The user can enter a new task through the menu.

Example:

```text
Enter new task: Complete Python Assignment
```

The task is added with a **Pending** status.

### 2. View Tasks

The application displays all stored tasks along with their current status.

Example:

```text
========== TASK LIST ==========

1. ❌ Complete Python Assignment
2. ✅ Buy Groceries
3. ❌ Finish Project

===============================
```

### 3. Mark Task as Completed

The user selects a task number, and its status changes from **Pending** to **Completed**.

### 4. Delete Task

The user can select a task number to permanently remove it from the task list.

### 5. Save Tasks

Task information is automatically saved inside `tasks.txt`.

Example:

```text
Pending|Complete Python Assignment
Done|Buy Groceries
Pending|Finish Project
```

When the application starts again, the saved tasks are automatically loaded.

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check your Python installation using:

```bash
python --version
```

### Step 2: Open the Project Folder

Open a terminal inside the `To_Do_List` folder.

### Step 3: Run the Application

```bash
python todo.py
```

---

## 📋 Application Menu

```text
=====================================
        TO-DO LIST MENU
=====================================

1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit

=====================================
```

---

## 🎯 Learning Objectives

This project demonstrates the following Python concepts:

* **File Handling** — reading and writing task data
* **Lists** — storing multiple tasks
* **Dictionaries** — storing task information and status
* **Functions** — organizing application logic
* **CRUD Operations** — Create, Read, Update, and Delete
* **Loops** — keeping the application running
* **Conditional Statements** — handling user choices
* **Input Validation** — preventing invalid user input

---

## 🔮 Future Improvements

The application can be extended with:

* 🔍 Search tasks by keyword
* 📅 Add due dates
* ⭐ Add task priorities
* 📊 Display productivity statistics
* 🗑️ Clear all completed tasks
* ⏰ Sort tasks by priority or due date
* 🖥️ Create a graphical user interface
* 🗄️ Replace the text file with SQLite or another database

---

## 👨‍💻 Author

**Kartik Malik**

A Python-based beginner project demonstrating task management, CRUD operations, and file handling.
