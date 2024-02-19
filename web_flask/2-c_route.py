#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """returns hbnb"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return 'HBNB!'

@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """returns C with the passed variable"""
    text_with_spaces = escape(text.replace('_', ' '))
    return f'C {text_with_spaces}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
