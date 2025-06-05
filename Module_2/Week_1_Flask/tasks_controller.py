import json
import os

FILE_PATH = "data.json"

def read_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def get_tasks_by_status(status=None):
    tasks = read_tasks()
    if status:
        return [t for t in tasks if t["status"] == status]
    return tasks

def create_task(new_task):
    tasks = read_tasks()
    tasks.append(new_task)
    save_tasks(tasks)

def update_task(id, new_data):
    tasks = read_tasks()
    for task in tasks:
        if task["id"] == id:
            task.update(new_data)
            save_tasks(tasks)
            return True
    return False

def delete_task(id):
    tasks = read_tasks()
    new_tasks = [t for t in tasks if t["id"] != id]
    if len(new_tasks) == len(tasks):
        return False
    save_tasks(new_tasks)
    return True
