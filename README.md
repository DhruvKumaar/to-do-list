# To-Do List App

## Overview

A simple command-line To-Do List application written in Python that allows you to manage your daily tasks with features like add, edit, delete, mark as done, and view tasks. All tasks are stored in a local `tasks.txt` file.

## Features

- Add a new task with optional priority and due date
- Edit existing tasks
- Delete tasks
- Mark tasks as done
- View all tasks with status, priority, and due date
- Data stored in a human-readable `.txt` file (no database required)

## Files

- `to_do.py` — Main Python script containing the application logic
- `tasks.txt` — Stores the tasks in text format (created automatically if not present)

## Task Format

Each task is stored as a line in `tasks.txt` using the format:

```
Title|Done|Priority|DueDate
```

**Example:**

```
Buy groceries|False|medium|10-07-2025
```

## Technology Used

- **Python 3.x** (Core Language)
- File Handling (Read/Write operations)

## How to Run

1. Make sure you have Python installed.
2. Open terminal or command prompt.
3. Navigate to the folder containing `to_do.py`.
4. Run the application using:

```bash
python to_do.py
```

## Notes

- The app uses a plain `.txt` file, making it lightweight and easy to use.
- Priorities and due dates are optional.
- It’s a good beginner project to learn file handling, functions, and user interaction in Python.
