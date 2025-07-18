from random import randint

from util.storage import save_to_json_file


def generate_task_id(tasks):
    existing_ids = [task["id"] for task in tasks]

    new_id = randint(1, 9999)
    while new_id in existing_ids:
        new_id = randint(1, 9999)
    return new_id


def add_new_task(tasks, task_name):
    new_task = {"id": generate_task_id(tasks), "task": task_name, "completed": False}
    tasks.append(new_task)
    save_to_json_file(tasks)
    print("Task added")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("There are currently no tasks.")
    else:
        for task in tasks:
            status = "not completed"
            if task["completed"] is True:
                status = "completed"
            print(f"ID:{task["id"]} : {task["task"]} : {status}")


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_to_json_file(tasks)
            print("Task marked as completed")
            break
    else:
        print('ID not found')


def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_to_json_file(tasks)
            print("Task successfully removed")
            break
    else:
        print('ID not found')
