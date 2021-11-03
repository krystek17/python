#!/usr/bin/env python3

string = input("Enter the string: ").lower().replace(" ", "").replace(",", "")
check = set(string)
if len(check) == 26:
    print("This is a pangram")
else:
    print("try again")
