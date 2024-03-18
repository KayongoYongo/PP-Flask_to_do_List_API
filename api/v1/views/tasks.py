from api.v1.views import app_views
from flask import request, jsonify, abort
from models.tasks import Tasks
from db import DB

@app_views.route('/tasks',
                 methods=['POST'], strict_slashes=False)
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

    # Create an instance of the DB class
    db = DB()

    # Add a task using the add_task method
    db.add_task(**data)

    return jsonify({'message': 'Task added successfully'})