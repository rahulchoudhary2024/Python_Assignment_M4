'''Write a Python program to copy the contents of a file to another file.'''

file=open("tops.txt","r")
file1=open("tops10.txt","w")
file1.write(file.read())
print("File copied successfully!")
file.close()
file1.close()
