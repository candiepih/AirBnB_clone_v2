#!/usr/bin/python3
"""
    Starts a flask web application listening on 0.0.0.0, port 5000
    and displays the results of states and their cities via
    "/cities_by_states" route
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


@app.route("/cities_by_states")
def states_cities_route():
    """
        Route that fetches all cities in a stage
        from the storage engine
    """
    states = storage.all(State)
    all_states = []

    for state in states.values():
        cities = state.cities
        cities_list = list(filter(lambda x: x.state_id == state.id, cities))
        c_data = list(map(lambda x: [x.id, x.name], cities_list))
        all_states.append([state.id, state.name, c_data])

    return render_template("8-cities_by_states.html", states=all_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
