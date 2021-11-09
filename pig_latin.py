#!/usr/bin/env python3

words = input("Please enter a sentence: ").lower().strip().split()
latin = []

for word in words:
    if word[0] in "aeiou":
        latin.append(word + "yay")
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        latin.append(new_word)

output = " ".join(latin)
print(output)
