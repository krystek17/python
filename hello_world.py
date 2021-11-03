#!/usr/bin/env python3

name = input("What is your name? ").strip().title()
output = "Hello {}".format(name)

if not name == "":
    print(output)
else:
    print("Hello World")
