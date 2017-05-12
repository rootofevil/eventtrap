from app import db
from datetime import datetime
from sqlalchemy.sql.elements import Null
#from sqlalchemy.orm import backref, relationship

class event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    category = db.Column(db.String(50))
    computer = db.Column(db.String(20))
    description = db.Column(db.String(250))
    datetime = db.Column(db.DateTime)
    
    def __init__(self, title, computer):
        self.title = title
        self.computer = computer
        self.datetime = datetime.now()
        
        