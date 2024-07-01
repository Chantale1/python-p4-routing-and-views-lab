#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:to_print>')
def print_string(to_print):
    print(to_print)
    return to_print

@app.route('/count/<int:number>')
def count(number):
    result = '\n'.join(str(n) for n in range(number))
    return result

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        if num2 != 0:
            return str(num1 / num2)
        else:
            return 'Division by zero is not allowed.'
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Operation not recognized. Please use one of the following: + - * div %'

if __name__ == '__main__':
    app.run(port=5555, debug=True)

