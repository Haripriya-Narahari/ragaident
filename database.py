from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask_session import Session
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///./database.sqlite3")
Session = scoped_session(sessionmaker(bind=engine))
engine = None
session = Session()
Base = declarative_base()
db = SQLAlchemy()
