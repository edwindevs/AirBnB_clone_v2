#!/usr/bin/python3
'''
script to start flask web application framework
'''

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def print_hello():
    '''printing Hello HBNB'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def print_hbnb():
    '''printing HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_variable(text):
    '''printing variable argument
    replace _ with a space
    '''
    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_default(text='is cool'):
    '''default value of text -> is cool
    replace _ with a space
    '''
    return 'Python %s' % text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''displays n only if n is an integer'''
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
