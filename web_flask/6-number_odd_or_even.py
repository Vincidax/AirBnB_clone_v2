#!/usr/bin/python3
"""
Flask web application with specific routes and templates
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!' on the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' on the /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Displays 'C ' followed by the value of text
    (replace underscore _ symbols with a space)"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<path:text>', strict_slashes=False)
def python_route(text):
    """Displays 'Python ' followed by the value of text
    (replace underscore _ symbols with a space)"""
    text = text.replace('_', ' ') if text else 'is cool'
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Displays 'n is a number' only if n is an integer"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page if n is an integer"""
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)
    else:
        return 'Not Found', 404


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page indicating if n is even or odd"""
    if isinstance(n, int):
        odd_or_even = 'odd' if n % 2 != 0 else 'even'
        return render_template('6-number_odd_or_even.html',
                               n=n, odd_or_even=odd_or_even)
    else:
        return 'Not Found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
