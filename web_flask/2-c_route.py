#!/usr/bin/python3
"""
Module for a Flask web application with specific routes.
"""

from flask import Flask

app = Flask(__name__)


def hello():
    """
    Route to display 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


def hbnb():
    """
    Route to display 'HBNB'.
    """
    return 'HBNB'


def show_c_text(text):
    """
    Route to display 'C ' followed by the value of the text variable.
    Replaces underscores with spaces.
    """
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/')
def index():
    """
    Route for the main page.
    """
    return hello()


@app.route('/hbnb')
def display_hbnb():
    """
    Route to display 'HBNB'.
    """
    return hbnb()


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """
    Route to display 'C ' followed by the value of the text variable.
    Replaces underscores with spaces.
    """
    return show_c_text(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
