#!/usr/bin/python3
"""
    a script that starts
    flask web application
    Returns:
            Hello HBNB!
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "<p>Hello HBNB!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)