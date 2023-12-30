#!/usr/bin/python3
"""
This module demonstrates a simple Flask application.

It defines a Flask app with a single route that displays
'Hello HBNB!' when accessed.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!' when the root URL is accessed.

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
