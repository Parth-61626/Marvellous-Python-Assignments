# 1) Write a program which accepts one number and checks whether it is prime or not

n = int(input("Enter number :"))

data = []

for i in range(1,n+1):
    if n % i == 0:
        data.append(i)

if len(data) == 2:
    print("Prime Number")

# 2) Write a program which accepts one number and prints count of digits in that number

num = int(input("Enter the number :"))
count = 0

if num == 0 :
    count = 1
else:
    while num > 0:
        count = count + 1
        num = num // 10

print(count)


# 3) Write a program which accepts one number and prints sum of digits

no = int(input("Enter a number :"))

ans = 0

while no > 0:
    ans = ans + no % 10
    no = no // 10

print("Addition of digits is",ans)

# 4) Write a program which accepts one number and prints reverse of that number

number1 = int(input("Enter a number :"))

reverse = 0

while number1 > 0:
    reverse = reverse * 10 + number1 % 10
    number1 = number1 // 10

print("Reverse is :",reverse)


# 5) Write a number program which accepts one number and checks whether it is palindrome or not

number2 = int(input("Enter a number :"))

reverse = 0

while number2 > 0:
    reverse = reverse * 10 + number1 % 10
    number2 = number2 // 10

print("Reverse is :",reverse)

if number2 == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")