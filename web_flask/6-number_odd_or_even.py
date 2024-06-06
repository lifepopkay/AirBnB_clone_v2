#!/usr/bin/python3
"""
    a script that starts
    flask web application
    Returns:
            Hello HBNB!
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "<p>Hello HBNB!</p>"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_display(text):
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_display(text='is cool'):
    return "python  " + text.replace('_', ' ')


@app.route("/number_template/<int:n>", strict_slashes=False)
def digit_temp(n):
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        t = "even"
    else:
        t = "odd"
    return render_template('6-number_odd_or_even.html',
                            number=n, nt=t)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
