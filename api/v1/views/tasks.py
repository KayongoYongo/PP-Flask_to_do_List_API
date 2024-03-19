from api.v1.views import app_views
from flask import request, jsonify, abort
from models.tasks import Tasks
from models import storage

@app_views.route('/tasks', methods=['GET'], strict_slashes=False)
def get_tasks():
    """
    Returns all tasks
    """
    task_objs = storage.all(Tasks)
    tasks = [obj.to_dict() for obj in task_objs.values()]
    # print(tasks)
    return jsonify(tasks), 200

@app_views.route('/tasks/<task_id>', methods=['GET'], strict_slashes=False)
def get_individual_tasks(task_id):
    """"
    Returns indivuidual users by id
    """
    task = storage.get(Tasks, task_id)

    print(task)
    if task is None:
        abort(404)
    return jsonify(task.to_dict()), 200

@app_views.route('/tasks', methods=['POST'], strict_slashes=False)
def create_tasks():
    """
    The function creates a task from the
    """
    # Get data from the request body
    data = request.get_json()

    if data is None:
        abort(400, 'Not a JSON')
    if data.get("title") is None:
        abort(400, 'Missing title')
    if data.get("status") is None:
        abort(400, 'Missing status')
    if data.get("description") is None:
        abort(400, 'Missing description')

    # Create an instance of the tasks class
    new_task = Tasks(**data)
    
    # Use the storage instance to interact with the database
    # Add the new task to the session
    storage.new(new_task)

    # Commit the transaction
    storage.save() 

    return jsonify(new_task.to_dict()), 201