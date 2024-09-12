#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [None] * list_length
    x = 0
    while x < list_length:
        try:
            new_list[x] = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            new_list[x] = 0
            print("division by 0")
        except IndexError:
            new_list[x] = 0
            print("out of range")
        except (TypeError, ValueError):
            new_list[x] = 0
            print("wrong type")
        x += 1
    return new_list
