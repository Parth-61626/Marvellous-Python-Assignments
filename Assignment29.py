import os
import sys

# 1)

file_name = input("Enter file name :")

print("File exists :",os.path.exists(file_name))


# 2)

file_name = input("Enter file name :")

obj1 = open(file_name,"r")
data = obj1.read()
print(data)


# 3)

file_name = sys.argv[1]

obj2 = open(file_name,"r")
r = obj2.read()

obj3 = open("Demo.txt","w")
obj3.write(r)


# 4)

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]

obj4 = open(file_name1,"r")
a = obj4.read()

obj5 = open(file_name2,"r")
b = obj5.read()

if a == b:
    print("Success")
else:
    print("Failure")


# 5)
Filename=sys.argv[1]
word=sys.argv[2]

f1=open(Filename,"r")
data=f1.read()
f1.close()

count=data.count(word)
print(data)