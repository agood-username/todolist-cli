tasks = []


def add_new_task(task_name):
    new_task = {
        "task": task_name, "completed": False
    }
    tasks.append(new_task)
    print("Task added")


def view_tasks():
    if len(tasks) == 0:
        print("There are currently no tasks.")
    else:
        for task in tasks:
            status = "not completed"
            if task["completed"] is True:
                status = "completed"
            print(f"{task["task"]} : {status}")


exit = False
print("Welcome to todolist-cli, enter help for a list of commands")
while exit is not True:

    choice = input(": ")
    match choice:
        case "help":
            print("Commands: view, add, delete, complete, quit")
        case "view":
            print(f"Task count: {len(tasks)}")
            view_tasks()
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
