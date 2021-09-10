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
    cities = State.cities
    all_states = []

    for state in states.values():
        cities_list = list(filter(lambda x: x.state_id == state.id, cities))
        c_data = list(map(lambda x: [x.id, x.name], cities_list))
        # c_data = [[city.id, city.name] for city in cities_list]
        all_states.append([state.id, state.name, c_data])

    return render_template("7-states_list.html", states=all_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
