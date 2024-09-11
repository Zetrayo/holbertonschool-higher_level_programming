#!/usr/bin/python3
def roman_to_int(roman_string):
    add = 0
    roman = ["I", "V", "X", "L", "C", "D", "M"]
    deci = [1, 5, 10, 50, 100, 500, 1000]
    for x in roman_string:
        for i in range(len(roman)):
            if x == roman[i]:
                if add < deci[i]:
                    add = deci[i] - add
                else:
                    add = deci[i] + add
    return add
