from .database import db
import pytz
from datetime import datetime


class Participant(db.Model):
    __tablename__ = 'participant'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    gender = db.Column(db.String(10), nullable = False)
    pass

class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    question_id = db.Column(db.Integer, nullable = False)
    choice = db.Column(db.Boolean(), nullable = False)
    participant_id= db.Column(db.Integer, db.ForeignKey('participant.id'))
    participant = db.relationship("Participant", backref="answers")
