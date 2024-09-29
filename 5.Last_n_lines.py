'''Write a Python program to read last n lines of a fil'''

n=int(input("Enter Lines"))
file=open("tops.txt","w")
file.write("This is file management.\nThis is file management.\nThis is file management.\nL5This is file management.\nL4This is file management.\nL3This is file management.\nL2This is file management.\nL1This is file management.")
print("File Written Successfully")
file=open("tops.txt","r")
x=file.readlines()
for i in range(-n,0):
    print(x[i],end="")
file.close()
