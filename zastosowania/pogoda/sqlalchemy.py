from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(80), unique=True, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username