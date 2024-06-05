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
@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    return "<p>Hello HBNB!</p>"

@app.route("/c/<text>",strict_slashes=False)
def text_to_display(text):
    return f"C {escape(text)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
