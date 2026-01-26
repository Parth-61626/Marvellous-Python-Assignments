# 1) Write a program which accept N numbers from user and stores it into List.Return addition of all elements from the List

from functools import reduce

data1 = []

size1 = int(input("Enter size of list :"))

for i in range(size1):
    value = int(input("Enter a value :"))
    data1.append(value)

def Addition(no1,no2):
    return no1 + no2

ans1 = reduce(Addition,data1)
print(ans1)

# OR

ans1 = 0

for i in range(size1):
    ans1 = ans1 + data1[i]

print(ans1)

# OR

ans1 = 0

for i in data1:
    ans1 = ans1 + i

print(ans1)


# 2) Write a program which accept N numbers from user and stores it into List.Return Maximum number from that list

from functools import reduce

data1 = []

size1 = int(input("Enter size of list :"))

for i in range(size1):
    value = int(input("Enter a value :"))
    data1.append(value)

def Maximum(no1,no2):
    if no1 > no2:
        return no1
    else:
        return no2

ans1 = reduce(Maximum,data1)
print(ans1)


# 3) Write a program which accept N numbers from user and stores it into List.Return Minimum number from that list

from functools import reduce

data1 = []

size1 = int(input("Enter size of list :"))

for i in range(size1):
    value = int(input("Enter a value :"))
    data1.append(value)

def Minimum(no1,no2):
    if no1 < no2:
        return no1
    else:
        return no2

ans1 = reduce(Minimum,data1)
print(ans1)


# 4 ) Write a program which accept N numbers from user and stores it into List.Accept one another number from user and return frequency
# of that number from list

data1 = []

size1 = int(input("Enter size of list :"))

for i in range(size1):
    value = int(input("Enter a value :"))
    data1.append(value)

chk_num = int(input("Enter a number :"))

count = 0

for i in range(size1):
    if data1[i] == chk_num:
        count = count + 1

print(f"Frequency of {chk_num} is : {count}")


# 5) Write a program which accept N numbers from user and store it into the list.Return addition of all prime numbers from that list.
# Main python file accepts N numbers from user and pass each number to ChkPrime() which is part of our user defined module named as
# MaevellousNum.Name of the function from main python file should be ListPrime()

import MarvellousNum

def ListPrime(no):
    sum = 0
    for i in no:
        if MarvellousNum.ChkPrime(i):
            sum = sum + i

    return sum

def main():
    data = []

    size = int(input("Enter size of list :"))

    for i in range(size):
        value = int(input("Enter a value :"))
        data.append(value)

    Ret = ListPrime(data)

    print("Addition of prime numbers is :",Ret)
    

if __name__ == "__main__":
    main()