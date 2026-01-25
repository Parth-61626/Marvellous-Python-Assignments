# 1) Write a  lambda function which accepts one number and returns square of that number

Square = lambda num1 : num1 ** 2

input1 = int(input("enter a number :"))
ans1 = Square(input1)
print("Square is :",ans1)


# 2) Write a lambda function which accepts one number and returns cube of that number

Cube = lambda num2 : num2 ** 3

input2 = int(input("enter a number :"))
ans2 = Cube(input2)
print("Cube is :",ans2)


# 3) Write a lambda function which accepts two numbers and returns maximum number

Maximum = lambda no1,no2 : no1 if no1>no2 else no2

i1 = int(input("enter first number :"))
i2 = int(input("enter second number :"))
ans3 = Maximum(i1,i2)
print("Maximum is :",ans3)


# 4) Write a lambda function which accepts two numbers and returns minimum number

Minimum = lambda n1,n2 : n1 if n1<n2 else n2

i_1 = int(input("enter first number :"))
i_2 = int(input("enter second number :"))
ans4 = Minimum(i_1,i_2)
print("Minimum is :",ans4)


# 5) Write a lambda function which accepts one number and returns True if number is even otherwise False

is_even = lambda x : x % 2 == 0

num3 = int(input("enter a number :"))
ans5 = is_even(num3)
print(ans5)


# 6) Write a lambda function which accepts one number and returns True if number is odd otherwise False

is_odd = lambda y : x % 2 != 0

num4 = int(input("enter a number :"))
ans6 = is_odd(num4)
print(ans6)


# 7) Write a lambda function which accepts one number and returns True if divisible by 5

divisible_by_5 = lambda z : z % 5 == 0

num5 = int(input("enter a number :"))
ans7 = divisible_by_5(num5)
print(ans7)


# 8) Write a lambda function which accepts two numbers and returns addition

add = lambda a,b : a+b

first_number = int(input("Enter a number :"))
second_number = int(input("Enter a number :"))

ans8 = add(first_number,second_number)
print("Addition is :",ans8)


# 9) Write a lambda function which accepts two numbers and returns multiplication

add = lambda a,b : a*b

first__number = int(input("Enter a number :"))
second__number = int(input("Enter a number :"))

ans9 = add(first__number,second__number)
print("Addition is :",ans9)


# 10) Write a lambda function which accepts three numbers and returns largest number

Greater_number = lambda d,e,f : d if (d >= e and d >= f) else (e if e >= f else f)

first___number = int(input("Enter a number :"))
second___number = int(input("Enter a number :"))
third___number = int(input("Enter a number :"))

ans10 = Greater_number(first___number,second___number,third___number)
print("Largest number is :",ans10)