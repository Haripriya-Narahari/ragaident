
from flask_restful import Resource, Api, fields, marshal_with
from flask import redirect
from flask_restful import reqparse
from model import *
from validation import *
from database import db
from sqlalchemy import select,update,delete
from flask_security.utils import  hash_password
from flask_security import auth_required
import uuid
import matplotlib.pyplot as plt
import os
import io
import base64
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np
from librosa import load,to_mono, hz_to_note, note_to_svara_c

login_fields = { 'username' : fields.String,
    'password' : fields.String,
    'usertitle' : fields.String,
    'active' : fields.Integer,
    'fs_uniquifier' : fields.String,
}

login_parser = reqparse.RequestParser()
login_parser.add_argument('username')
login_parser.add_argument('password')
login_parser.add_argument('usertitle')
login_parser.add_argument('active')
login_parser.add_argument('fs_uniquifier')

raga_fields = { 'uid' : fields.Integer,
    'r_name' : fields.String,
    'username' : fields.String,
    'date' : fields.String,
    'song_name' : fields.String,
}

raga_parser = reqparse.RequestParser()
raga_parser.add_argument('uid')
raga_parser.add_argument('r_name')
raga_parser.add_argument('username')
raga_parser.add_argument('date')
raga_parser.add_argument('song_name')

class UserLogin(Resource):
    @marshal_with(login_fields)
    def get(self):
        arg = login_parser.parse_args()
        username = arg.get("username",None)
        password = arg.get("password",None)
        if username is None:
            raise ValidationError(status_code=400,error_code='UE1001',error_message='Username is required')
        if password is None:
            raise ValidationError(status_code=400,error_code='UE1002',error_message='Password is required')
        log = db.session.query(Login).filter(Login.username == username).first()
        passwd = db.session.execute(select(Login.password).where(Login.username == username)).scalar()
        if passwd == password:
            return log

    
    @marshal_with(login_fields)
    def post(self):
        arg = login_parser.parse_args()
        username = arg.get("username",None)
        password = arg.get("password",None)
        usertitle = arg.get("usertitle",None)
        print(username,password,usertitle)
        if username is None:
            raise ValidationError(status_code=400,error_code='UE1001',error_message='Username is required')
        if password is None:
            raise ValidationError(status_code=400,error_code='UE1002',error_message='Password is required')
        user = db.session.query(Login).filter(Login.username == username).first()
        if user:
            raise ValidationError(status_code=400,error_code='UE1003',error_message='Username is used')
        uniq = uuid.uuid1().hex
        log = Login(username = username, password = hash_password(password), usertitle =usertitle, active=1, fs_uniquifier=uniq)
        print(log)
        db.session.add(log)
        db.session.commit()
        return "Success", 200


class UserInfo(Resource):
    @marshal_with(login_fields)
    @auth_required("token")
    def get(self,username):
        log = db.session.query(Login).filter(Login.username == username).scalar()
        return log
    
class RagaInfo(Resource):
    @marshal_with(raga_fields)
    @auth_required("token")
    def get(self,username):
        log = db.session.query(Raga).filter(Raga.username == username).all()
        return log


class RagaAdd(Resource):
    
    @marshal_with(raga_fields)
    #@auth_required("token")
    def post(self,username):
        arg = raga_parser.parse_args()
        r_name = arg.get("r_name",None)
        date = arg.get("date",None)
        song_name = arg.get("song_name",None)
        #username = arg.get("username",None)
        notes = arg.get('notes',None)
        notes = 'S,S,S,S,R'
        if song_name is None:
            raise ValidationError(status_code=400,error_code='RE1001',error_message='Song Name is required')
        
        print(song_name,r_name,username,date)
        log = Raga(username = username, r_name=r_name,date = date, song_name = song_name,notes=notes)
        db.session.add(log)
        db.session.commit()
        return log
    
    @marshal_with(raga_fields)
    @auth_required("token")
    def get(self,uid):
        log = db.session.query(Raga).filter(Raga.uid == uid).scalar()
        return log


class RagaDelete(Resource):
    @marshal_with(raga_fields)
    @auth_required("token")
    def get(self,uid):
        log = db.session.query(Raga).filter(Raga.uid == uid).scalar()
        return log
    
    @auth_required("token")
    def post(self,uid):
        arg = raga_parser.parse_args()
        uid = arg.get("uid",None)
        db.session.execute(delete(Raga).where(Raga.uid == uid))
        db.session.commit()
        return "Deleted"


class NotesGenerator(Resource):
    def post(self,file):
        file = "D:/MiniProject/"+file+'.wav'
        sampFreq_n, sound_n = wavfile.read(file)
        sound_n = sound_n[6000:7000]
        sound_n[sound_n<=0] = 1
        sound_n = np.abs(sound_n) / 2.0**15
        fft_spectrum_n= np.fft.rfft(sound_n)
        nn = hz_to_note(fft_spectrum_n[:,0])
        n_newn = np.array(nn)
        n_cn = note_to_svara_c(n_newn, Sa='C5',mela=22)
        notesn = np.array(n_cn)
        notesn = notesn[0:160]
        n_n = {}
        n_n['notes'] = notesn
        notess = ''
        i = 1
        for n in notesn:
            notess+= n+' , '
            if i % 4 == 0:
                notess+=" | "
            if i % 16 == 0:
                notess+="| \n"
            i+=1
        return notess

class RagaGenerator(Resource):
    def post(self,file):
        import pickle
        print(file)
        file = "D:/MiniProject/"+file+'.wav'
        filename = 'RagaModel.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        sampFreq_n, sound_n = wavfile.read(file)
        sound_n = sound_n[6000:7000]
        sound_n[sound_n<=0] = 1
        sound_n = np.abs(sound_n) / 2.0**15
        fft_spectrum_n= np.fft.rfft(sound_n)
        nn = hz_to_note(fft_spectrum_n[:,0])
        n_newn = np.array(nn)
        #mela = np.random.rndl
        n_cn = note_to_svara_c(n_newn, Sa='C5',mela=22)
        notesn = np.array(n_cn)
        import sklearn
        encodero = sklearn.preprocessing.OrdinalEncoder()
        encodero.fit(np.array(['S', 'R₁','R₂','R₃', 'G₁','G₂','G₃', 'M₁','M₂', 'P',  'D₁', 'D₂','D₃','N₁','N₂',  'N₃']).reshape(-1,1))
        an = encodero.transform(notesn.reshape(-1,1))
        e_notes = an[0:30].reshape(1,-1)
        e_notes = list(np.unique(e_notes))
        n_n = {}
        n_n['notes'] = np.unique(e_notes)
        print(n_n['notes'].resize(1,14))
        ra = loaded_model.predict(n_n['notes'].reshape(1, -1))
        return ra[0]

class GraphGenerator(Resource):
    def post(self,file):
        file = "D:/MiniProject/"+file+'.wav'
        f_b, sr = load(file)
        plt.plot(f_b)
        plt.xlabel("channel, sample #")
        plt.ylabel("Frequency")
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        plt.clf()
        img.seek(0)
        image_data = base64.b64encode(img.getvalue()).decode()
        plt.switch_backend('agg')
        return image_data
        