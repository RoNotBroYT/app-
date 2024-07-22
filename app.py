import os

# Define the file to store the tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the tasks file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = [line.strip() for line in file]
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save tasks to the tasks file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """Display the current list of tasks."""
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    """Remove a task from the list."""
    display_tasks(tasks)
    task_num = int(input("Enter the number of the task to remove: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number.")

def main():
    """Main function to run the to-do list app."""
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the to-do list manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
