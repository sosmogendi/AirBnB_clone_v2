#!/usr/bin/python3
"""
Start a Flask web application with multiple routes.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Define a route for the root URL ("/") that displays "Hello HBNB!"
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Define a route for "/hbnb" that displays "HBNB"
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Define a route for "/c/<text>" that displays "C ", followed by the value of the text variable.
    Replace underscores with spaces.
    """
    return "C " + text.replace("_", " ")

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
    Define a route for "/python/<text>" that displays "Python ", followed by the value of the text variable.
    Replace underscores with spaces. If text is not provided, use the default value "is cool".
    """
    return "Python " + text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Define a route for "/number/<n>" that displays "n is a number" only if n is an integer.
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
