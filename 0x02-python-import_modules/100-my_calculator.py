#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>", end="")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    """
    operator_functions = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
    }
    if operator in operator_functions:
        result = operator_functions[operator](a, b)
        print(f"{a} {operator} {b} = {result}")
    """
    if operator == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif operator == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif operator == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    elif operator == '/':
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /", end="")
        exit(1)
