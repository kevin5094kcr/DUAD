VALID_STATUSES = ["To Do", "In Progress", "Completed"]

def validate_new_task(task, existing_tasks):
    errors = []

    # Validate empty fields
    if "id" not in task or task["id"] == "":
        errors.append("The task must have an identifier.")
    if "title" not in task or task["title"].strip() == "":
        errors.append("The task must have a title.")
    if "description" not in task or task["description"].strip() == "":
        errors.append("The task must have a description.")
    if "status" not in task:
        errors.append("The task must have a status.")
    elif task["status"] not in VALID_STATUSES:
        errors.append(f"Invalid status. Use one of: {', '.join(VALID_STATUSES)}")

    # Check that the ID doesn’t already exist
    for existing in existing_tasks:
        if task["id"] == existing["id"]:
            errors.append("A task with that identifier already exists.")
            break

    return errors
