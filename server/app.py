#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>') 
def print_string(parameter):
    print(parameter)
    return f'{parameter}' 

@app.route('/count/<int:param>')
def count(param):
    numbers = '<br>'.join(str(i) for i in range(param))
    return f'<pre>{numbers}<pre>'

#alternatively horizontally
# @app.route('/count/<int:parameter>')
# def count(parameter):
#     return '\n'.join(map(str, range(parameter)))

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None 
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    elif operation == 'mod':
        result = num1 % num2 

    return f'<h1>Result of {num1} {operation} {num2}: {result}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
