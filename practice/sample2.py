#!/usr/bin/env python3.7

with open("test1.txt", "wt") as out_file:
    out_file.write("This text is going to out file\nlook at it and see!")

with open("test1.txt", "rt") as in_file:
    text = in_file.read()

print(text)
