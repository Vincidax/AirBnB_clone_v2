#!/usr/bin/python3
"""
Flask web application with specific routes
"""

from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Displays 'Hello HBNB!' on the root route
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' on the /hbnb route
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays 'C ' followed by the value of text
    (replace underscore _ symbols with a space)
    """
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<path:text>', strict_slashes=False)
def python_route(text):
    """
    Displays 'Python ' followed by the value of text
    (replace underscore _ symbols with a space)
    """
    text = text.replace('_', ' ') if text else 'is cool'
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Displays 'n is a number' only if n is an integer
    """
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
