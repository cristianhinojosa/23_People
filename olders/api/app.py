import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .models import *

# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:toor@localhost/api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# INIT DB
db = SQLAlchemy(app)

# init Marshmallow
ma = Marshmallow(app)




@app.route("/drugs/", endpoint="drugs", methods=["GET"])
def drugs_list():
    drugs = Drug.query.order_by(Drug.id).all()
    return jsonify({ "drugs": [{"name": x.name, "code": x.code, "description": x.description} for x in drugs]})





if __name__ == '__main__':
    app.run(debug=True)