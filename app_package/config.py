import os 

base_dir=os.path.abspath(os.path.dirname(__file__))
class Config(object):
   SECRET_KEY=os.urandom(24).hex()
   #SQLALCHEMY_DATABASE_URI="mysql+pymysql://flaskban:flaskban@localhost/bankdb"
   SQLALCHEMY_DATABASE_URI="mysql+pymysql://tamsuser:tamsuser@localhost/tamsdb"
   SQLALCHEMY_TRACK_MODIFICATIONS=False
   MONGO_URI="mongodb://localhost:27017/tamsdata"
    
