import os
#bdir = os.path.abspath(os.path.dirname(__file__))
class Config():
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SECURITY_TOKEN_AUNTHENTICATION_HEADER = "Authentication-Token"

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.sqlite3"
    SECRET_KEY =os.environ.get("Secret Key","qsqhj1g3h26")
    SECURITY_PASSWORD_SALT = os.environ.get("Security Password Salt","1221723151422")
    WTF_CSRF_ENABLED = False
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_USERNAME_ENABLE = True
    CORS_ORIGINS = "http://127.0.0.1:5000"
    CORS_RESOURCES = r"/*"
    
    SECURITY_USER_IDENTITY_ATTRIBUTES = ('username','email')
    
    
    
