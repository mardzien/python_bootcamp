from flask import Flask, render_template
from pogoda import get_location_id, get_location_weather, prepare_weather_report
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\kurs\workspace\python_bootcamp\stdlib\pogoda\test.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    return f"My wheader page"

@app.route("/<location_name>")
def weather(location_name):
    location_id = get_location_id(location_name)
    weather = get_location_weather(location_id)
    return render_template("index.html", weather=weather)

@app.route("/<history>")
def weather():
    weather = Weather.query.all()
    return render_template("history.html", weather=weather)

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.Text, unique=True, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Text, nullable=False)

if __name__ == "__main__":
    app.run()