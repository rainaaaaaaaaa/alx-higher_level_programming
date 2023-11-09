#!/usr/bin/python3
a = 10
b = 5

from calculator_1 import add, subtract, multiply, divide

result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)

print(f"{a} + {b} = {result_add}")
print(f"{a} - {b} = {result_subtract}")
print(f"{a} * {b} = {result_multiply}")
print(f"{a} / {b} = {result_divide}")
