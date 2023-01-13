from urllib import response
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from requests import get,post,patch,delete
from flask import current_app as app
from model import *
from api import *
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask_security import login_required, auth_required  

from database import db
import uuid
engine = create_engine("sqlite:///./database.sqlite3")

@app.route('/dashboard/<string:username>/<file>/') # the route name, <file> is like a request.args
def css(username,file):
  return render_template(file)

@app.route('/', methods = ['POST','GET'])
def landn():
    return render_template('landing.html')
       
@app.route('/loginpage', methods = ['POST','GET'])
def login():
    return render_template('login.html')

@app.route('/newuser', methods = ['POST','GET'])
def newuser():
    return render_template("newuser.html")

@app.route('/dashboard/<string:username>/', methods = ['POST','GET'])
@auth_required("token")
def dashboard(username):
    return render_template("dashboard.html")

@app.route('/ragaidentify', methods = ['POST','GET'])
def raga():
    return render_template("identify.html")

@app.route('/summary/<string:username>/', methods = ['POST','GET'])
@auth_required("token")
def summary(username):
    return render_template("summary.html")

@app.route('/howitworks', methods = ['POST','GET'])
#@auth_required("token")
def working():
    return render_template("howitworks.html")


