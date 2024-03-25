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

    if task is None:
        abort(404)
    return jsonify(task.to_dict()), 200

@app_views.route('/tasks', methods=['POST'], strict_slashes=False)
def create_tasks():
    """
    The function creates a task
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
    new_task.save()

    return jsonify(new_task.to_dict()), 201

@app_views.route('/tasks/<task_id>', methods=['PUT'], strict_slashes=False)
def update_tasks(task_id):
    """
    This function updates a task based on the ID
    """
    task = storage.get(Tasks, task_id)

    if task is None:
        abort(404)

    my_dict = request.get_json()

    if my_dict is None:
        abort(400, 'Not a JSON')

    for k, v in my_dict.items():
        setattr(task, k, v)

    storage.save()
    return jsonify(task.to_dict()), 200

@app_views.route('/tasks/<task_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(task_id):
    """
    Deletes individual tasks by id
    """
    task = storage.get(Tasks, task_id)

    if task is None:
        abort(404)

    # Deletes the task
    storage.delete(task)
    storage.save()
    return jsonify({}), 200