from flask import Flask, request, jsonify
from tasks_controller import (
    get_tasks_by_status,
    create_task,
    update_task,
    delete_task,
    read_tasks
)
from validators import validate_new_task

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    status = request.args.get("status")  # e.g., ?status=In%20Progress
    tasks = get_tasks_by_status(status)
    return jsonify(tasks), 200

@app.route("/tasks", methods=["POST"])
def add_task():
    new_task = request.json
    current_tasks = read_tasks()

    errors = validate_new_task(new_task, current_tasks)
    if errors:
        return jsonify({"errors": errors}), 400

    create_task(new_task)
    return jsonify({"message": "Task added successfully."}), 201

@app.route("/tasks/<id>", methods=["PUT"])
def edit_task(id):
    data = request.json
    updated = update_task(id, data)
    if updated:
        return jsonify({"message": "Task updated."}), 200
    return jsonify({"error": "Task not found."}), 404

@app.route("/tasks/<id>", methods=["DELETE"])
def remove_task(id):
    deleted = delete_task(id)
    if deleted:
        return jsonify({"message": "Task deleted."}), 200
    return jsonify({"error": "Task not found."}), 404

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
