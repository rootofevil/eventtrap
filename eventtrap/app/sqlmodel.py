from app import db, ma
from datetime import datetime, date
from sqlalchemy.sql.elements import Null
#from sqlalchemy.orm import backref, relationship

class event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    category = db.Column(db.String(50))
    computer = db.Column(db.String(20))
    status = db.Column(db.String(12))
    description = db.Column(db.String(250))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    
    def __init__(self, title, computer, status = 'info'):
        self.title = title
        self.computer = computer
        self.status = status
        self.date = date.today()
        self.time = datetime.now().time()
        
class eventSchema(ma.ModelSchema):
    class Meta:
        model = event