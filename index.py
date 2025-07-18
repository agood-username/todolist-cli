from util.storage import load_from_json_file
from util.todo_methods import add_new_task, delete_task, complete_task, view_tasks


def main():
    tasks = load_from_json_file()
    exit = False

    print("Welcome to todolist-cli, enter help for a list of commands")

    while exit is not True:
        choice = input("command: ")

        match choice:
            case "help":
                print("Commands: view, add, delete, complete, quit")
            case "view":
                print(f"Task count: {len(tasks)}")
                view_tasks(tasks)
            case "add":
                task = input("Add new task: ")
                add_new_task(tasks, task)
            case "delete":
                try:
                    id = int(input("Enter task ID: "))
                    delete_task(tasks, id)
                except ValueError:
                    print("Invalid input! Please enter a number")
            case "complete":
                try:
                    id = int(input("Enter task ID: "))
                    complete_task(tasks, id)
                except ValueError:
                    print("Invalid input! Please enter a number")
            case "quit":
                exit = True
            case _:
                print("Unknown command")


if __name__ == "__main__":
    main()