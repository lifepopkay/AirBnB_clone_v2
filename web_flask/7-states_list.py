#!/usr/bin/python3
"""
    A flask web application
    Display list of states
"""
from flask import Flask, render_template
from models.state import State
from models import *


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_html():
    """ Function called with /states_list route """
    states = storage.all(State)
    dict_to_html = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html',
                           Table="States",
                           items=dict_to_html)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
