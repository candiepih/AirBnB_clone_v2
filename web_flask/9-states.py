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


@app.route("/states")
@app.route("/states/<string:id>")
def states_cities_route(id):
    """
        Route that fetches all states or a certain state if exists
        or not
    """
    states = storage.all(State)
    all_states = []

    if id is None:
        for state in states.values():
            all_states.append([state.id, state.name])
        return render_template("8-cities_by_states.html",
                               states=all_states, id=id)
    else:
        state = list(filter(lambda x: x.id == id, states.values()))
        c_data = None
        if state[0]:
            cities = state[0].cities
            cities_list = list(filter(lambda x: x.state_id == state.id, cities))
            c_data = list(map(lambda x: [x.id, x.name], cities_list))
        return render_template("8-cities_by_states.html",
                               state=state[0], cities=c_data, id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
