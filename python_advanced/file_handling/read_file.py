#!/usr/bin/env python3
""" Python’s input/output mechanisms focusing on file manipulation"""

def read_file(filename=""):
    """ a function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, "r",encoding="UTF8") as file:
        print(file.read(),end="")

