#!/usr/bin/env python3

word = input("Please write a word: ")
items = input("Please write a list of words: ").split()
print("\n")
def anagram(word,items):
    output = []

    for i in items:
        if sorted(i) == sorted(word):
            output.append(i)
    return output

output = anagram(word,items)

for each in output:
    print(each + "\n")
