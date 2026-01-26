# 1) Write a program which contains one lambda function which accepts one parameter and return power of two

Square = lambda no : no ** 2

num = int(input("Enter a number :"))

print(Square(num))


# 2) Write a program which contains one lambda function which accepts two parameters and returns its multiplication

mult = lambda no1,no2 : no1 * no2

num1 = int(input("Enter a number :"))
num2 = int(input("Enter a number :"))

print(mult(num1,num2))

# 3) Write a program which contains filter(),map() and reduce() in it.A list contains values accepted from the user.
# Filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90.
# Map function will increase each number by 10.
# Reduce will return product of all that numbers.

from functools import reduce

data1 = []

size1 = int(input("Enter size of list :"))

for i in range(size1):
    value = int(input("Enter a value :"))
    data1.append(value)

print(data1)

def chk1(no):
    return 90 >= no >= 70

def Increment(no):
    no = no + 10
    return no

def product(no1,no2):
    return no1 * no2

fdata1 = list(filter(chk1,data1))
print("Data after filter :",fdata1)

mdata1 = list(map(Increment,fdata1))
print("Data after map :",mdata1)

rdata1 = reduce(product,mdata1)
print("Data after reduce :",rdata1)


# 4) Write a program which contains filter(),map() and reduce() in it.A list contains values accepted from the user.
# Filter should filter out all such numbers which are even.
# Map function will calculate its square.
# Reduce will return addition of all that numbers.

data2 = []

size2 = int(input("Enter size of list :"))

for i in range(size2):
    value = int(input("Enter a value :"))
    data2.append(value)

print(data2)

def chk2(no):
    return no % 2 == 0

def Square(no):
    return no ** 2

def sum(no1,no2):
    return no1 + no2

fdata2 = list(filter(chk2,data2))
print("Data after filter :",fdata2)

mdata2 = list(map(Square,fdata2))
print("Data after map :",mdata2)

rdata2 = reduce(sum,mdata2)
print("Data after reduce :",rdata2)


# 5) Write a program which contains filter(),map() and reduce() in it.A list contains values accepted from the user.
# Filter should filter out all prime numbers.
# Map function will multiply each number by 2.
# Reduce will return maximum number from that numbers.

data3 = []

size3 = int(input("Enter size of list :"))

for i in range(size3):
    value = int(input("Enter a value :"))
    data3.append(value)

print(data3)

def Prime(no):
    if no < 2:
        return False
    for i in range(2,int(no/2)+1):
        if no % i == 0:
            return False
    return True
    
def Mult(no1):
    return no1 * 2

def max(no1,no2):
    if no1 > no2:
        return no1
    else:
        return no2
    
fdata3 = list(filter(Prime,data3))
print("Data after filter :",fdata3)

mdata3 = list(map(Mult,fdata3))
print("Data after map :",mdata3)

rdata3 = reduce(max,mdata3)
print("Data after reduce :",rdata3)