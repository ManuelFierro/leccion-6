import random
import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
     ahora =  datetime.datetime.now()
     añonuevo = (ahora.month == 1) and (ahora.day == 1)
     headline = random.choice(["hola mundo","que onda","que pex","buenos dias"])
     return render_template("index.html", new_year=añonuevo)

@app.route("/bye")
def bye():
     headline = "ADIOS"
     return render_template("index.html",headline= headline)


