#!/usr/bin/env python3

name = input("What is your name? ").strip().title()

if not name == "":
    print("Hello {}".format(name))
else:
    print("Hello World")
