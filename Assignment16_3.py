# Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers

def Add(no1,no2):
    return no1 + no2

def main():
    num1 = int(input("enter a number :"))
    num2 = int(input("enter a number :"))

    result = Add(num1,num2)
    print("Addition is :",result)

if __name__ == "__main__":
    main()