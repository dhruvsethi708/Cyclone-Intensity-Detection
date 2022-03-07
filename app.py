from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///intensity.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Intensity(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    intensity = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.intensity}"




@app.route("/")
def hello_world():
    intensity_cal = Intensity(intensity=10.2)
    db.session.add(intensity_cal)
    db.session.commit()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)