#!/usr/bin/env python3

words = input("Please enter a sentence: ").lower().strip().split()
latin = []

for word in words:
    if word[0] in "aeiou":
        latin.append(word + "yay")
    else:
        vowel = 0
        for letter in word:
            if letter not in "aeiou":
                vowel = vowel + 1
            else:
                break
        cons = word[:vowel]
        rest = word[vowel:]
        latin.append(rest + cons + "ay")

output = " ".join(latin)
print(output)
