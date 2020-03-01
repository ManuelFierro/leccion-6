from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/mas")
def mas():
     return render_template("mas.html")

@app.route("/bye")
def bye():
     headline = "ADIOS"
     return render_template("index.html",headline= headline)


