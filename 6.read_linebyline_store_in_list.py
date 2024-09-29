'''Write a Python program to read a file line by line and store it into a list'''

file=open("tops.txt","r")
l1=[]
for i in file:
    l1.append(i.strip())
print(l1)

print("---------------")

filename = "tops.txt"  
file_list = []

with open(filename, "r") as file:
    for line in file:
        file_list.append(line.strip())

print(file_list)
