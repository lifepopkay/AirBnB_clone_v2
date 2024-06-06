#!/usr/bin/python3
"""
    A flask web application    
"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route("/states_list")
def states_list():
    """display a HTML page"""
    states = storage.all(State).values()
    sort_states = sorted(states, key=lambda x: x.name)
    render_template('7-states_list.html',
                    state=sort_states)


@app.teardown_appcontext
def close_session(exception):
    """Close the storage"""
    storage.close()
    

