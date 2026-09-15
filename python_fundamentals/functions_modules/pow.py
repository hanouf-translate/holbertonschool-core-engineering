#!/usr/bin/env python3

def pow(a, b):
    result = 1
    for _ in range(b):
        result = result * a
    return result
