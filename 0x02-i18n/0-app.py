#!/usr/bin/env python3
"""Setup Basic flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Returns a simple template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
