#!/usr/bin/env python3

import string

def pangram(s):
    alphabet = string.ascii_lowercase
    for i in alphabet:
        if i not in s.lower():
            return False
    return True

sentence = input()
if pangram(sentence):
    print("This is a pangram")
else:
    print("Try again")
