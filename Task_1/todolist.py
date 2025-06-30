# Empty list to store tasks
tasks = []

# Function to show all tasks
def show_tasks():
    pending_tasks = [t for t in tasks if not t["done"]]
    if not pending_tasks:
        print("No pending tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(pending_tasks, 1):
            print(f"{i}. {task['task']} [✗ Not Done]")
    print()


# Function to add a task
def add_task():
    task_desc = input("Enter the task: ")
    tasks.append({"task": task_desc, "done": False})
    print("Task added!\n")

# Function to delete a task
# def delete_task():
#     show_tasks()
#     try:
#         task_no = int(input("Enter task number to delete: "))
#         if 1 <= task_no <= len(tasks):
#             removed = tasks[task_no]
#             print(f"Deleted task: {removed['task']}\n")
#         else:
#             print("Invalid task number.\n")
#     except ValueError:
#         print("Please enter a valid number.\n")

def delete_task():
    pending_tasks = [t for t in tasks if not t["done"]]
    if not pending_tasks:
        print("No pending tasks to delete.\n")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(pending_tasks, 1):
        print(f"{i}. {task['task']} [✗ Not Done]")
    print()

    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(pending_tasks):
            task_to_remove = pending_tasks[task_no - 1]
            tasks.remove(task_to_remove)  # remove from main list
            print(f"Deleted task: {task_to_remove['task']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


# Function to mark a task as done
def mark_done():
    show_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["done"] = True
            print("Task marked as done!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


# Main loop
while True:
    print("----- To-Do List Menu -----")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.\n")
