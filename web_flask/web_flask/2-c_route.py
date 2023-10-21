#!/usr/bin/python3
"""
Start a Flask web application with two routes.
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
	Define a route for "/c/<text>" that displays "C" followed by the value
	of the text variable. Replace underscores with spaces.
	"""
	return "C " + text.replace("_", " ")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
