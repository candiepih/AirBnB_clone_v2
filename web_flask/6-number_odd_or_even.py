from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<string:text>")
def c_route(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<string:text>")
def py_route(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def n_route(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def n_template_route(n):
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_even_route(n):
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
