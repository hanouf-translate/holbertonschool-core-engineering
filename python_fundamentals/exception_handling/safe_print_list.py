#!/usr/bin/env python3


def safe_print_list(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except IndexError:
            break
    print()
    return counter
# if __name__ =="__main__":
#     my_list = [1, 2, 3, 4, 5]
#     nb_print = safe_print_list(my_list, 2)
#     print(f"elements: {nb_print}")