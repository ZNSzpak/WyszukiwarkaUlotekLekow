from flask import Flask, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Leki(db.Model):
    NazwaProduktuLeczniczego = db.Column(db.String(100), primary_key=True)
    Ulotka = db.Column(db.String(100), nullable=False)
    

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("indexRP.html")

@main.route("/search")
def search():
    q = request.args.get("q")
    print(q)

    if len(q)>=4:
        resultsALL = list(Leki.query.filter(Leki.NazwaProduktuLeczniczego.icontains(q)))
        results = resultsALL[:10]
    else:
        results = []

    return render_template("search_resultsRP.html", results=results)

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///RP.db"

    db.init_app(app)

    app.register_blueprint(main)

    return app



