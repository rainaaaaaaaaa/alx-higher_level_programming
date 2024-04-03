#!/usr/bin/python3
def uppercase(s):
    result = ""
    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            result += "{}".format(chr(ord(c) - ord('a') + ord('A')))
        else:
            result += "{}".format(c)
    print(result)
