from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean
from database import Base
from database import db
from flask_security import UserMixin,RoleMixin


class Login(db.Model, UserMixin):
    __tablename__ = 'login'

    id = Column(Integer,nullable=False, primary_key = True,autoincrement=True)
    username = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    usertitle = Column(String,nullable=False)
    active = Column(Boolean,nullable=False)
    fs_uniquifier = Column(String,unique = True, nullable=False)

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    roleid = Column(Integer,nullable=False, primary_key = True,autoincrement=True)
    name = Column(String,nullable=False)
    description = Column(String,nullable=False)

class Raga(db.Model):
    __tablename__ = 'raga'
    uid = Column(Integer,nullable=False, primary_key = True,autoincrement=True)
    r_name = Column(String)
    username = Column(String, ForeignKey("login.username"))
    date = Column(String, nullable=False)
    song_name = Column(String, nullable=False)
    notes = Column(String,nullable=False)

