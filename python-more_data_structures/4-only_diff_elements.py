#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uniq = list(set(set_1).symmetric_difference(set_2))
    return uniq