from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Enum

"""
By inheriting from Base, the User class inherits all the features 
provided by Base, such as metadata management, reflection, 
and other ORM-related functionalities. This approach makes 
it easier to manage and work with database models in SQLAlchemy.
"""
Base = declarative_base()

class Task(Base):

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(Enum('todo', 'done'), default='todo')