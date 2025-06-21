#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Title view at base URL
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:input_string>')
def print_string(input_string):
    # Print to console and display in browser
    print(input_string)
    return input_string

@app.route('/count/<int:number>')
def count(number):
    # Display numbers from 0 up to number-1, each on a new line
    return '\n'.join(str(i) for i in range(number)) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    # Perform basic arithmetic based on operation parameter
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        # Division, using 'div' to avoid URL slash conflict
        if num2 == 0:
            return 'Error: Division by zero'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
