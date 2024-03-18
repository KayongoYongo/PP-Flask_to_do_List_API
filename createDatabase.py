from db import DB  # Import the DB class
from models.tasks import Base  # Import the declarative base
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Instantiate the DB object
db_instance = DB()

# Create tables using SQLAlchemy's create_all() method
Base.metadata.create_all(db_instance._engine)

print("Tables created successfully")

"""
NOTE:
SQLAlchemy doesn't handle database creation directly; 
it assumes that the database already exists. 
So, if you try to create tables without the database being present, 
it will result in an error.
"""