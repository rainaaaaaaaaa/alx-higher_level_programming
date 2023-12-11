#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    i = len(argv)
    print(f"{i-1} argument", end="")
    if i == 1:
        print("s.")
    elif i == 2:
        print(":")
    else:
        print("s:")
    for j in range(1, i):
        print("{j}: {argv[j]}")
