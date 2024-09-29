'''Write a Python program to write a list to a file.'''

l1=[1,2,3,4,5]

file=open("tops5.txt","w")

for i in l1:
    file.write(str(i))
file.close()
print("Done")
