from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from models.tasks import Tasks

# Load environment variables from the .env file
load_dotenv()

# Create declarative base
Base = declarative_base()

class DB:

    def __init__(self) -> None:
        """The function initializes a new DB instance
        """
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        host = os.getenv('HOST')
        port = os.getenv('PORT')
        database = os.getenv('DATABASE')

        # Print the loaded environment variables
        print("USERNAME:", username)
        print("PASSWORD:", password)
        print("HOST:", host)
        print("PORT:", port)
        print("DATABASE:", database)
        
        # This line sets the database URI for SQLAlchemy to connect to the databse
        mysql_url = f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}'

        # Its primary purpose is to manage the details of how to connect to the database        
        self._engine = create_engine(mysql_url, echo=False)

        # This session attribute will be used to store a session object later.
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            #  It creates a new session object (DBSession) using sessionmaker and binds it to the engine 
            DBSession = sessionmaker(bind=self._engine)
            # This session object is then stored in the __session attribute.
            self.__session = DBSession()
        return self.__session
    
    def add_task(self, **kwargs) -> Tasks:
        """
        The function adds a task to the database

        Args:
            **kwargs: The function accepts a variable number of
            key worded arguments.

        Returns:
            Task: The newly created task object
        """
        task = Tasks(**kwargs)
        self._session.add(task)
        self._session.commit()
        return task