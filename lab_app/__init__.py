import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    reviewtext = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.title[:10])

with app.app_context():
    db.create_all()

from .routes import *
