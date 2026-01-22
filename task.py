# create a cli to create task, view tasks, save task to a file, load task from file, delete task

# create task
tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if tasks:
        print("\nYour tasks:")
        for task in tasks:
            print(f"{task}")
    else:
        print("No tasks yet!")

def main():
    while True:
        print("\n1. Add task\n2. View tasks\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

main()




# view task


# save task to a file


# load task from file


# delete task