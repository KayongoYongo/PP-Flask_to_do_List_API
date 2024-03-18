from db import DB
from models.tasks import Tasks  # Import the Tasks model

# Create an instance of the DB class
db = DB()

# Define task data
task_data = {
    'title': 'Complete project',
    'description': 'Finish coding the project',
    'status': 'todo'  # Note: Assuming status can only be 'todo' or 'done'
}

# Add a task using the add_task method
new_task = db.add_task(**task_data)

# Print the newly created task
print("New Task:")
print("ID:", new_task.id)
print("Title:", new_task.title)
print("Description:", new_task.description)
print("Status:", new_task.status)