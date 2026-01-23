# Simple Task Manager (Beginner Version)

tasks = []

# Menu
def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Save tasks to file")
    print("5. Load tasks from file")
    print("6. Exit")

# Adding tasks
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

# Viewing tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

# Deleting tasks
def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number to delete: "))
        tasks.pop(number - 1)
        print("Task deleted!")
    except:
        print("Invalid input.")

# Saving tasks
def save_tasks():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()
    print("Tasks saved to tasks.txt")

# Loading tasks
def load_tasks():
    global tasks
    try:
        file = open("tasks.txt", "r")
        tasks = file.read().splitlines()
        file.close()
        print("Tasks loaded from tasks.txt")
    except:
        print("No file found.")


# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        save_tasks()
    elif choice == "5":
        load_tasks()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
