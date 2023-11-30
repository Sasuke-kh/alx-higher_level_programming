#!/usr/bin/python3
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def magic_calculation(a, b):
    c = add(a, b) if a < b else sub(a, b)

    if a < b:
        for i in range(4, 7):
            c = add(c, i)

    return c
