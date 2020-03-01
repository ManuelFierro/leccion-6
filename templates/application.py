from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
     headline = "holaa, mundo!"
     hola = "hola que hace equis de equis de"
     return render_template("index.html", headline=hola)

@app.route("/bye")
def bye():
     headline = "ADIOS"
     return render_template("index.html",headline= headline)


