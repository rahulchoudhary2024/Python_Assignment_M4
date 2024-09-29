'''Write a python program to find the longest words.'''

import re

l1="abc abcd abcde"
word=r'\w+'
sub=re.findall(word,l1)
max_word=max(sub,key=len)
print(max_word)


print("-----------------")

import re

l1="abc abcd abcde"
word=r'\w+'
sub=re.findall(word,l1)
max_len = 0
max_word = ""

for w in sub:
    if len(w) > max_len:
        max_len = len(w)
        max_word = w

print(max_word) 
