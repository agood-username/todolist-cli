# tasks = []

# task = input('Add task: ')
# newTask = {"taskName": task, "completed": False}
# tasks.append(newTask)

# print(f"{task} added to list.")

# print(tasks[0])


tasks = []


def add_new_task(task_name):
    new_task = {
        "task": task_name, "completed": False
    }
    tasks.append(new_task)
    print("Task added")


exit = False
print("Welcome to todolist-cli, enter help for a list of commands")
while exit is not True:

    choice = input(": ")
    match choice:
        case "help":
            print("Commands: view, add, delete, complete, quit")
        case "view":
            print("This is for viewing tasks")
        case "add":
            task = input("Add new task: ")
            add_new_task(task)
        case "delete":
            print("This is for deleting task")
        case "complete":
            print("This is for completing task")
        case "quit":
            exit = True
        case _:
            print("Unknown command")
