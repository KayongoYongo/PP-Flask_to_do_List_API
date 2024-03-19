from models import storage
from models.tasks import Tasks  # Import the Tasks model

# Define task data
task_data = {
    'title': 'Test project',
    'description': 'Finish fixing the project',
    'status': 'todo'  # Note: Assuming status can only be 'todo' or 'done'
}

# Add a task using the add_task method
new_task = Tasks(**task_data)

# Use the storage instance to interact with the database
# Add the new task to the session
storage.new(new_task)

# Commit the transaction
storage.save() 

# Print the newly created task
print("New Task:")
print("ID:", new_task.id)
print("Title:", new_task.title)
print("Description:", new_task.description)
print("Status:", new_task.status)