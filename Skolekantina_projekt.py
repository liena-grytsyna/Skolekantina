from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "nbQ&UdC%TwrmU#Z9WG2n3nY2tc4@f$fUay@MDmy?qg??3v*tSHyfR4qjMMnM8aJD"

app.config["SQLALCHEMY_DATABASE_URI"] = "mariadb+mariadbconnector://Oleksandr:root@10.0.0.85:3308/Skolekantina"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Meny_uke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uke = db.Column(db.String(200))
    mandag = db.Column(db.String(200))
    tirsdag = db.Column(db.String(200))
    onsdag = db.Column(db.String(200))
    torsdag = db.Column(db.String(200))
    fredag = db.Column(db.String(200))

@app.route("/")
def home():
    username = "gigachad"
    return render_template("martynas.html", username=username)


@app.route("/vika_screen")
def vika_screen():
    return render_template("/vika_screen/index.html")

@app.route("/liena")
def liena():
    return render_template("/liena-website/index.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8245, debug=True)