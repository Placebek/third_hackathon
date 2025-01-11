from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from envenv import DATABASE
Base = declarative_base()

class DatabaseManager:
    def __init__(self):
        self.engine = create_engine(DATABASE)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

        
        