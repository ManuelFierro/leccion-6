import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
     headline = random.choice(["hola mundo","que onda","que pex","buenos dias"])
     return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
     headline = "ADIOS"
     return render_template("index.html",headline= headline)


