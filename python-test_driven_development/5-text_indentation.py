#!/usr/bin/python3
def text_indentation(text):
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for x in text:
        if i > 0:
            i = 0
            continue
        if x == "." or x == "?" or x == ":":
            print("{}".format(x))
            print()
            i += 1
            continue
        print("{}".format(x), end="")
