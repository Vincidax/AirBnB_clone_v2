#!/usr/bin/python3
"""
Starts a Flask web application with specified routes.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!" on the root route.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Display "HBNB" on the /hbnb route.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """
    Display "C " followed by the value of the text variable.
    Replace underscores with spaces.
    """
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """
    Display "Python " followed by the value of the text variable.
    Replace underscores with spaces.
    If no text is provided, default to "is cool".
    """
    text = text.replace('_', ' ') if text else 'is cool'
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
