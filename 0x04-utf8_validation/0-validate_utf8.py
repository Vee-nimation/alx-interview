#!/usr/bin/python3
"""
Function file
"""


def validUTF8(data):
    """Method that determines if a given data set represents a
        valid UTF-8 encoding.
        array data: set of integers
    Return: true if the set of data is utf-8 else false
    """

    count = 0
    for byte in data:
        if 128 <= byte <= 191:
            if count == 0:
                return False
            count -= 1
        else:
            if count:
                return False
            if byte < 128:
                continue
            elif byte < 224:
                count = 1
            elif byte < 240:
                count = 2
            elif byte < 248:
                count = 3
            else:
                return False
    return count == 0
