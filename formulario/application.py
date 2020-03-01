from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/hola", methods=["GET","POST"])
def hola():
          name = request.form.get("name")
          return render_template("hola.html",name=name)

@app.route("/bye")
def bye():
     headline = "ADIOS"
     return render_template("index.html",headline= headline)


