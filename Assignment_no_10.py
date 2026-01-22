# 1) Write a program which accepts one number and prints multiplication table of that number

n = int(input("Enter number :"))

for i in range(1,11):
    print(n*i)

# 2) Write a program which accepts one number and prints sum of first N natural numbers

n = int(input("Enter number :"))

sum = 0

for i in range(n+1):
    sum = sum + i

print("Sum :",sum )

# 3) Write a program which accepts one number and prints factorial of that number

n = int(input("Enter number :"))

factorial = 1

for i in range(1,n+1):
    factorial = factorial * i

print("Factorial is :",factorial)

# 4) Write a program which accepts one number and prints all even numbers till that number

n = int(input("Enter number :"))

for i in range(2,n+1,2):
    print(i)

# OR

n = int(input("Enter number :"))

for i in range(1,n+1):
    if i % 2 == 0:
        print(i)


# 5) Write a program which accepts one number prints all odd numbers till that number

n = int(input("Enter number :"))

for i in range(n+1):
    if i % 2 == 1:
        print(i)