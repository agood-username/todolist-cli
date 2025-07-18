from random import randint

import storage

tasks = storage.load_from_json_file()


def generate_task_id():
    existing_ids = [task["id"] for task in tasks]

    new_id = randint(1, 9999)
    while new_id in existing_ids:
        new_id = randint(1, 9999)
    return new_id


def add_new_task(task_name):
    new_task = {"id": generate_task_id(), "task": task_name, "completed": False}
    tasks.append(new_task)
    storage.save_to_json_file(tasks)
    print("Task added")


def view_tasks():
    if len(tasks) == 0:
        print("There are currently no tasks.")
    else:
        for task in tasks:
            status = "not completed"
            if task["completed"] is True:
                status = "completed"
            print(f"ID:{task["id"]} : {task["task"]} : {status}")


def log_method_decorator(func):
    def log_method(*args, **kwargs):
        view_tasks()
        func(*args, **kwargs)
    return log_method


@log_method_decorator
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            storage.save_to_json_file(tasks)
            print("Task marked as completed")
            break
    else:
        print('ID not found')


@log_method_decorator
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            storage.save_to_json_file(tasks)
            print("Task successfully removed")
            break
    else:
        print('ID not found')


exit = False
print("Welcome to todolist-cli, enter help for a list of commands")
while exit is not True:

    choice = input("command: ")
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
            try:
                id = int(input("Enter task ID: "))
                delete_task(id)
            except ValueError:
                print("Invalid input! Please enter a number")
        case "complete":
            try:
                id = int(input("Enter task ID: "))
                complete_task(id)
            except ValueError:
                print("Invalid input! Please enter a number")
        case "quit":
            exit = True
        case _:
            print("Unknown command")
