#!/usr/bin/python3
"""
    Contains a file that starts a Flask web application
    and displays “Hello HBNB!” at "/"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloholberton():
    """
        Display “Hello HBNB!” on "/" route
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
