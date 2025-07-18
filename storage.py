import json


def load_from_json_file():
    with open("tasks.json") as f:
        tasks = json.load(f)
        f.close()
        return tasks


def save_to_json_file(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2, sort_keys=True)
        f.close()
