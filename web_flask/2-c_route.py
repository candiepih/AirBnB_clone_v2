#!/usr/bin/python3
"""
    script that starts a Flask web application:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text
    variable (replace underscore _ symbols with a space)
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """
        Display “Hello HBNB!” on "/" route
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
        Display “HBNB!” on "/" route
    """
    return "HBNB"


@app.route("/c/<string:text>")
def c_route(text):
    """
        Display “C ” followed by the value of the text
        variable (replace underscore _ symbols with a
        space )
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
