import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db():
    """
    Connect to the database and return a connection object.
    """
    db = sqlite3.connect("tasks.db")
    db.row_factory = sqlite3.Row # Setting the `row_factory` attribute to `sqlite3.Row` to allow each row to be treated as a dictionary
    return db

@app.route("/create_task", methods=["POST"])
def create_task():
    """
    Create a new task in the database.

    The task description is passed in the request body as a JSON object.
    Returns a JSON object with the message "Task created successfully" if the task was created successfully,
    or an error message if there was a problem.
    """
    task = request.get_json()
    if not task:
        return {"error": "description requires"}
    try:
        db = get_db()
        db.execute("INSERT INTO tasks (description, completed) VALUES (?,?)",
               (task["description"], task.get("completed", False)))
        db.commit()
        return {"message": "Task created successfully"}
    except sqlite3.Error as err:
        return {"error" : str(err)}

@app.route("/delete_task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    Delete a task from the database.

    The task ID is passed in the URL.
    Returns a JSON object with the message "Task deleted successfully" if the task was deleted successfully,
    or an error message if there was a problem.
    """

    try:
        db = get_db()
        db.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        db.commit()
        return {"message": "Task deleted successfully"}
    except sqlite3.Error as err:
        return {"error" : str(err)}

@app.route("/update_task/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """
    Update a task in the database.

    The task ID is passed in the URL, and the updated task description and completion status are passed in the request body as a JSON object.
    Returns a JSON object with the message "Task updated successfully" if the task was updated successfully,
    or an error message if there was a problem.
    """
    task = request.get_json()
    db = get_db()
    db.execute("UPDATE tasks SET description=?, completed=? WHERE id=?",
               (task["description"], task.get("completed", False), task_id))
    db.commit()
    return {"message": "Task updated successfully"}

@app.route("/mark_task/<int:task_id>/complete", methods=["PUT"])
def mark_task_complete(task_id):
    """
    Mark a task as complete in the database.

    The task ID is passed in the URL.
    Returns a JSON object with the message "Task marked as complete" if the task was marked as complete successfully,
    or an error message if there was a problem.
    """
    try:
        db = get_db()
        db.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
        db.commit()
        return {"message": "Task marked as complete"}
    except sqlite3.Error as err:
        return {"error" : str(err)}

@app.route("/mark_task/<int:task_id>/incomplete", methods=["PUT"])
def mark_task_incomplete(task_id):
    """
    Mark a task as incomplete in the database.

    The task ID is passed in the URL.
    Returns a JSON object with the message "Task marked as uncomplete" if the task was marked as incomplete successfully,
    or an error message if there was a problem.
    """
    try:
        db = get_db()
        db.execute("UPDATE tasks SET completed=0 WHERE id=?", (task_id,))
        db.commit()
        return {"message": "Task marked as incomplete"}
    except sqlite3.Error as err:
        return {"error" : str(err)}

@app.route("/get_tasks", methods=["GET"])
def get_tasks():
    """
    Retrieve a list of all tasks stored in the database.
    
    Returns a JSON response containing a list of tasks, each represented as a dictionary.
    """
    db = get_db()
    tasks = db.execute("SELECT * FROM tasks").fetchall()
    return {"tasks": [dict(task) for task in tasks]}

@app.errorhandler(404)
def not_found():
    """
    Handle 404 errors by returning a JSON response with a message of "Not Found".
    
    Return a JSON response with a status code of 404.
    """
    return jsonify({'message': 'Not Found'}), 404

if __name__ == '__main__':
    db = get_db()
    db.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT, completed BOOLEAN)")
    app.run()
