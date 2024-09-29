'''Write a Python program to count the number of lines in a text file.'''

file=open("tops.txt","r")
lines=file.readlines()
print(len(lines))
