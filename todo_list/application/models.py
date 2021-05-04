from application import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(50), default = 'No description')
    complete = db.Column(db.Boolean, default = False)

