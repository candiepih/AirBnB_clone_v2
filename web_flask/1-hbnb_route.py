#!/usr/bin/python3
"""
    Script that starts a Flask web application:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
