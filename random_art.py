import random
from math import sin, cos, pi, sqrt

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

def geometric_mean(*args):
    multiplicative_sum = 1
    for arg in args:
        multiplicative_sum *= (abs(arg) +1)
    return pow(multiplicative_sum, -len(args))

def avg(*args):
    return sum(args) / len(args)

def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    function_list = []
    function_list.append(lambda x, y: sqrt(abs(y) + 1))
    function_list.append(lambda x, y: avg(sin(x) * cos(pi *y)))
    function_list.append(lambda x, y: avg(sin(x), cos(y)))
    function_list.append(lambda x, y: sin(pi * (sin(y /2) * 2) - 1 + cos(x) * geometric_mean(x, y)))
    function_list.append(lambda x, y: sin(x * sin(y)) + avg(0.5, x))
    expr = random.choice(function_list)
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""

    return expr(x, y)
