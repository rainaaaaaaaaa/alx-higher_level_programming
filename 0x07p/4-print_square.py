#!/usr/bin/python3

def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for a in range(0, size):
            for b in range(0, size):
                print("#", end="")
            print()
