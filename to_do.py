TASKS_FILE = "tasks.txt"

tasks = []

def load_tasks():
    global tasks
    tasks = []
    try:
        with open(TASKS_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 4:
                    title, done, priority, due_date = parts
                    task = {
                        "title": title,
                        "done": done == "True",
                        "priority": priority if priority != "None" else None,
                        "due_date": due_date if due_date != "None" else None
                    }
                    tasks.append(task)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open(TASKS_FILE, 'w') as f:
        for task in tasks:
            line = f"{task['title']}|{task['done']}|{task.get('priority', 'None')}|{task.get('due_date', 'None')}\n"
            f.write(line)

def show_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{idx + 1}. [{status}] {task['title']} (Priority: {task.get('priority', 'None')}, Due: {task.get('due_date', 'None')})")

def add_task():
    title = input("Task title: ")
    priority = input("Priority (low/medium/high or leave blank): ").strip()
    due_date = input("Due date (dd-mm-yyyy or leave blank): ").strip()

    task = {
        "title": title,
        "done": False,
        "priority": priority if priority else None,
        "due_date": due_date if due_date else None
    }
    tasks.append(task)
    save_tasks()
    print("Task added.")

def edit_task():
    show_tasks()
    index = int(input("Enter task number to edit: ")) - 1
    if 0 <= index < len(tasks):
        title = input("New title (leave blank to keep current): ")
        priority = input("New priority (leave blank to keep current): ")
        due_date = input("New due date (dd-mm-yyyy or leave blank): ")
        
        if title:
            tasks[index]["title"] = title
        if priority:
            tasks[index]["priority"] = priority
        if due_date:
            tasks[index]["due_date"] = due_date
        save_tasks()
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task():
    show_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks()
        print("Task deleted.")
    else:
        print("Invalid task number.")

def mark_task():
    show_tasks()
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks()
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def menu():
    while True:
        print("\n--- To-Do List ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Mark task as done")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_task()
        elif choice == '6':
            print("Exiting!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    load_tasks()
    menu()