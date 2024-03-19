from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Enum

"""
By inheriting from Base, the User class inherits all the features 
provided by Base, such as metadata management, reflection, 
and other ORM-related functionalities. This approach makes 
it easier to manage and work with database models in SQLAlchemy.
"""
Base = declarative_base()

class Tasks(Base):

    __tablename__ = 'todo_table'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(Enum('todo', 'done'))

    def __init__(self, title, description, status='todo'):
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict
    
    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Status: {self.status}"