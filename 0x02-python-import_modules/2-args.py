#!/usr/bin/python3
import sys

if __name__ == "__main":
    argc = len(sys.argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
