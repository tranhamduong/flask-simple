from app import db
import random


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone_number = db.Column(db.String(11))
    image = db.Column(db.String(255))
    

    
    jackpot_keys = db.Column(db.String(4))

    def __init__(self, name, phone_number, image, jackpot_keys):
        self.name = name  
        self.phone_number = phone_number
        self.image = image
        self.jackpot_keys =  jackpot_keys

    def __repr__(self):
        return '<User %r>' % self.name
