import random
import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
     nombres =  ["Alicia", "Eloisa", "Carlos"]
     headline = random.choice(["hola mundo","que onda","que pex","buenos dias"])
     return render_template("index.html", names=nombres)

@app.route("/bye")
def bye():
     headline = "ADIOS"
     return render_template("index.html",headline= headline)


