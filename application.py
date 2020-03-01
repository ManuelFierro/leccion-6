from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
     return "hello, world!"


@app.route("/david")
def david():
     return "hello, david!"

@app.route("/maria")
def maria():
     return "hello, maria!"

@app.route("/<string:name>")
def hello(name):
     return f"hello, {name}!"

