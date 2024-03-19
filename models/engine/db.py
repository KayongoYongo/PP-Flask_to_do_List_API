from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from models.tasks import Tasks
from sqlalchemy.orm import scoped_session, sessionmaker

# Load environment variables from the .env file
load_dotenv()

# Create declarative base
Base = declarative_base()

classes = {"Tasks": Tasks}

class DB:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """The function initializes a new DB instance
        """
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        host = os.getenv('HOST')
        port = os.getenv('PORT')
        database = os.getenv('DATABASE')
        
        # This line sets the database URI for SQLAlchemy to connect to the databse
        mysql_url = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}'

        # Its primary purpose is to manage the details of how to connect to the database        
        self.__engine = create_engine(mysql_url, echo=False)
    
    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)
    
    def get(self, cls, id):
        """A method to retrieve one object"""
        my_dict = self.all(cls)
        for obj in my_dict.values():
            if obj.id == id:
                return obj

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session