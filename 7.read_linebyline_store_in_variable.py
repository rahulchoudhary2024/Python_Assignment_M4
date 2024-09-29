'''Write a Python program to read a file line by line store it into a variable'''

file=open("tops.txt","r")
lines=file.readlines()
print(lines)

print("--------------------------")
filename = "tops.txt"

with open(filename, "r") as file:
    line1 = file.readline().strip()
    line2 = file.readline().strip()
    line3 = file.readline().strip()

print(line1)
print(line2)
print(line3)
