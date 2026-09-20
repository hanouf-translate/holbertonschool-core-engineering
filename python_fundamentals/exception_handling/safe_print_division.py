#!/usr/bin/env python3


def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result


# if __name__ == "__main__":
#     safe_print_division(10, 2)
#     safe_print_division(10, 0)
#     safe_print_division(10, 5)