from app import db

#Create BD Class Named Drug
class Drug(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(255), unique=False)
       code = db.Column(db.String(10), unique=True)
       description = db.Column(db.String(255), unique=False)
       
       def __init__(self, username, email):
           self.name = name
           self.code = code
           self.description = description

       def __repr__(self):
           return '<Drug %r>' % self.name

#Create BD Class Named Vaccination
class Vaccination(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       rut = db.Column(db.String(255), unique=False)
       dose = db.Column(db.String(10), unique=True)
       date = db.Column(db.DateTime, unique=False)
       drug = db.Column(db.Integer, db.ForeignKey('drug.id'), nullable=False)
       
       def __init__(self, username, email):
           self.name = name
           self.code = code
           self.description = description

       def __repr__(self):
           return '<Vaccination  id %r>' % self.id

#Create BD Class Named User
class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(80), unique=True)
       email = db.Column(db.String(120), unique=True)

       def __init__(self, username, email):
           self.username = username
           self.email = email

       def __repr__(self):
           return '<User %r>' % self.username