#!/usr/bin/python3
"""
    Starts a flask web application listening on 0.0.0.0, port 5000
    and displays the results of states via "/states_list" route
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_context(exception):
    """
        These functions are typically also called when the request
        context is popped.
    """
    storage.close()


@app.route("/states_list")
def states_route():
    """
        Route that fetches all states from the storage engine
    """
    states = storage.all(State)
    all_states = []

    for state in states.values():
        all_states.append([state.id, state.name])

    return render_template("7-states_list.html", states=all_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
