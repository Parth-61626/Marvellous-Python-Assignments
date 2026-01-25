from functools import reduce


# 1) Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number

squares = lambda no1 : no1 ** 2

data1 = []
size1 = int(input("Enter size of the list :"))

for i in range(size1):
    value = int(input("Enter element :"))
    data1.append(value)

print(data1)

mdata1 = list(map(squares,data1))
print("Square :",mdata1)

# OR

data1 = []
size1 = int(input("Enter size of the list :"))

for i in range(size1):
    value = int(input("Enter element :"))
    data1.append(value)

print(data1)

mdata1 = list(map(lambda no1 : no1 ** 2,data1))
print("Square :",mdata1)


# 2) Write a lambda function using filter() which accepts a list of numbers a returns a list of even numbers

is_even = lambda no2 : no2 % 2 == 0

data2 = []
size2 = int(input("Enter size of the list :"))

for i in range(size2):
    value = int(input("enter element :"))
    data2.append(value)

print(data2)

fdata1 = list(filter(is_even,data2))
print(fdata1)

# OR

data2 = []
size2 = int(input("Enter size of the list :"))

for i in range(size2):
    value = int(input("enter element :"))
    data2.append(value)

print(data2)

fdata1 = list(filter(lambda no2 : no2 % 2 == 0,data2))
print(fdata1)


# 3) Write a lambda function using filter() which accepts a list of numbers a returns a list of odd numbers

is_odd = lambda no2 : no2 % 2 != 0

data3 = []
size3 = int(input("Enter size of the list :"))

for i in range(size3):
    value = int(input("enter element :"))
    data3.append(value)

print(data3)

fdata2 = list(filter(is_odd,data3))
print(fdata2)

# OR

data3 = []
size3 = int(input("Enter size of the list :"))

for i in range(size3):
    value = int(input("enter element :"))
    data3.append(value)

print(data3)

fdata2 = list(filter(lambda no2 : no2 % 2 != 0,data3))
print(fdata2)

# 4) Write a lambda function using reduce() which accepts a list of numbers a returns the addition of all the elements

add = lambda a,b : a+b

data4 = []
size4 = int(input("Enter size of the list :"))

for i in range(size4):
    value = int(input("enter element :"))
    data4.append(value)

rdata1 = reduce(add,data4)
print("Addition is :",rdata1)

# OR

data4 = []
size4 = int(input("Enter size of the list :"))

for i in range(size4):
    value = int(input("enter element :"))
    data4.append(value)

rdata1 = reduce(lambda a,b : a+b,data4)
print("Addition is :",rdata1)

# 5) Write a lambda function using reduce() which accepts a list of numbers a returns the maximum element

maximum = lambda c,d : c if c>d else d

data5 = []
size5 = int(input("Enter size of the list :"))

for i in range(size5):
    value = int(input("enter element :"))
    data5.append(value)

rdata2 = reduce(maximum,data5)
print("Maximum :",rdata2)

# OR

data5 = []
size5 = int(input("Enter size of the list :"))

for i in range(size5):
    value = int(input("enter element :"))
    data5.append(value)

rdata2 = reduce(lambda c,d : c if c>d else d,data5)
print("Maximum :",rdata2)


# 6) Write a lambda function using reduce() which accepts a list of numbers a returns the minimum element

minimum = lambda c,d : c if c<d else d

data6 = []
size6 = int(input("Enter size of the list :"))

for i in range(size6):
    value = int(input("enter element :"))
    data6.append(value)

rdata3 = reduce(minimum,data6)
print("Minimum :",rdata3)

# OR

data6 = []
size6 = int(input("Enter size of the list :"))

for i in range(size6):
    value = int(input("enter element :"))
    data6.append(value)

rdata3 = reduce(lambda c,d : c if c<d else d,data6)
print("Minimum :",rdata3)


# 7) Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5

check = lambda string : len(string) > 5

data7 = []
size7 = int(input("Enter size of the list :"))

for i in range(size7):
    value = input("enter element :")
    data7.append(value)

fdata3 = list(filter(check,data7))
print("List of strings :",fdata3)

# OR

data7 = []
size7 = int(input("Enter size of the list :"))

for i in range(size7):
    value = input("enter element :")
    data7.append(value)

fdata3 = list(filter(lambda string : len(string) > 5,data7))
print("List of strings :",fdata3)


# 8) Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5

div_check = lambda num : num % 3 == 0 and num % 5 == 0

data8 = []
size8 = int(input("Enter size of the list :"))

for i in range(size8):
    value = int(input("enter element :"))
    data8.append(value)

fdata4 = list(filter(div_check,data8))
print("List of num :",fdata4)

# OR

data8 = []
size8 = int(input("Enter size of the list :"))

for i in range(size8):
    value = int(input("enter element :"))
    data8.append(value)

fdata4 = list(filter(lambda num : num % 3 == 0 and num % 5 == 0,data8))
print("List of num :",fdata4)


# 9) Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements

product = lambda a,b : a*b

data9 = []
size9 = int(input("Enter size of the list :"))

for i in range(size9):
    value = int(input("enter element :"))
    data9.append(value)

rdata4 = reduce(product,data9)
print("Product is :",rdata4)

# OR

data9 = []
size9 = int(input("Enter size of the list :"))

for i in range(size9):
    value = int(input("enter element :"))
    data9.append(value)

rdata4 = reduce(lambda a,b : a*b,data9)
print("Product is :",rdata4)


# 10) Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers

is_even_count = lambda no2 : no2 % 2 == 0

data10 = []
size10 = int(input("Enter size of the list :"))

for i in range(size10):
    value = int(input("enter element :"))
    data10.append(value)

print(data10)

fdata5 = list(filter(is_even_count,data10))
print(fdata5)

print("The count of even numbers is :",len(fdata5))

# OR

data10 = []
size10 = int(input("Enter size of the list :"))

for i in range(size10):
    value = int(input("enter element :"))
    data10.append(value)

print(data10)

fdata5 = len(list(filter(lambda no2 : no2 % 2 == 0,data10)))

print("The count of even numbers is :",fdata5)