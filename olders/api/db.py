from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from models import Drug, Vaccination, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:toor@localhost/api'
db = SQLAlchemy(app)





admin = User('admin', 'admin@example.com')

db.create_all() # In case user table doesn't exists already. Else remove it.    

db.session.add(admin)

db.session.commit() # This is needed to write the changes to database

User.query.all()

User.query.filter_by(username='admin').first()
