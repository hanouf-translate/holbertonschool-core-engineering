#!/usr/bin/env python3


def safe_print_list(my_list=[], x=0):
    try:
        
        counter = 0
        for element in my_list:

            print("{:d}".format(element) ,end =" ")
            counter += 1 
            if element > x:
                return counter

    except IndexError:
        print(f"You reached the last element")
        

if __name__ =="__main__":
    my_list = [1, 2, 3, 4, 5]
    nb_print = safe_print_list(my_list, 2)
    print(f"elements: {nb_print}")