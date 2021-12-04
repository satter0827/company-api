import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.dirname(__file__)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Company(db.Model):
  __tablename__ = 'persons'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  description = db.Column(db.String(128), nullable=False)
  url = db.Column(db.String(128), nullable=False)