# 1) Write a program which accepts one character and checks whether it is vowel or consonant

char = input("Enter character :")

if char in ("a","e","i","o","u"):
    print("Character is vowel")
else:
    print("Character is consonant")

# 2) Write a program which accepts one number and print its factors

n = int(input("Enter number :"))

for i in range(1,n+1):
    if n % i == 0:
        print(i)

# 3) Write a program which accepts two numbers and prints addition,subtraction,multiplication and division

def addition(no1,no2):
    sum = no1 + no2
    return sum

def subtraction(no1,no2):
    difference = no1 - no2
    return difference

def multiplication(no1,no2):
    product = no1 * no2
    return product

def division(no1,no2):
    division = no1/no2
    return division

def main():
    print("Enter first number :")
    num1 = int(input())
    print("Enter second number :")
    num2 = int(input())

    ans1 = addition(num1,num2)
    print("Addition is :",ans1)

    ans2 = subtraction(num1,num2)
    print("Subtraction is :",ans2)

    ans3 = multiplication(num1,num2)
    print("Multiplication is :",ans3)

    ans4 = division(num1,num2)
    print("Division is :",ans4)

if __name__ == "__main__":
    main()


# 4) Write a program which accepts one number and prints that many numbers starting from 1

num = int(input("Enter number :"))

for i in range(1,num+1):
    print(i)


# 5) Write a program which accepts one number and prints that many numbers in reverse order

num = int(input("Enter number :"))

for i in range(num,0,-1):
    print(i)