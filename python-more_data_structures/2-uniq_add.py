#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    my_set = set(my_list)
    new_list = list(my_set)
    for x in range(len(new_list)):
        add = new_list[x] + add
    return add
