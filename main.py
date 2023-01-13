from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from sqlalchemy import func
import os
from database import db
from flask_security import Security, SQLAlchemySessionUserDatastore
#from database import db
from flask_session import Session
from model import *
from flask_restful import Resource, Api
from config import DevelopmentConfig
from flask_cors import CORS
from sqlalchemy.orm import scoped_session, sessionmaker
app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
engine = create_engine("sqlite:///./database.sqlite3")
#Session = scoped_session(sessionmaker(bind=engine))
db.init_app(app)
api = Api(app)
#session = Session()
user_datastore = SQLAlchemySessionUserDatastore(db.session, Login, Role)
CORS(app,  supports_credentials=True)

from api import *
api.add_resource(UserLogin, "/api/newuser")
api.add_resource(UserInfo, "/api/<string:username>")
api.add_resource(RagaDelete, "/api/raga/<int:uid>/delete" )
api.add_resource(RagaInfo, "/api/raga/<string:username>" )
api.add_resource(RagaAdd, "/api/ragadd/<string:username>" )
api.add_resource(NotesGenerator, "/api/notes/<string:file>")
api.add_resource(GraphGenerator, "/api/graph/<string:file>")
api.add_resource(RagaGenerator, "/api/ragagen/<string:file>")

if __name__ == '__main__':
    
    security = Security(app, user_datastore)
    
    api.init_app(app)
    
    with app.app_context():
        from controllers import *
        db.create_all()
        app.run()
        
