from application import db

class Elves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    skill_Level = db.Column(db.Integer, nullable=False)
    workshop = db.relationship('Workshop', backref='workshop')

class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    toy_making =  db.Column(db.String(30), nullable=False)
    toy_design = db.Column(db.String(30), nullable=False)
    toy_wrapping = db.Column(db.String(30), nullable=False)
    workshop_id = db.Column(db.Integer, db.ForeignKey('elves.id'), nullable=False)