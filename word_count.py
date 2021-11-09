#!/usr/bin/env python3

from collections import Counter
words = input("Enter your sentence: ").split()
count = dict(Counter(words))

for k, v in count.items():
    print(k,":",v)
