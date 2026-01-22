# 1) Write a program which contains one function named as Display() that prints "Jay Ganesh" on console
def Display():
    print("Jay Ganesh")

Display()


# 2) Write a program which contains one function chkGreater() that accepts two numbers and prints the greater number
def chkGreater():
    no1 = int(input("Enter first number :"))
    no2 = int(input("Enter second number :"))
    
    if no1 > no2:
        print(no1,"is greater")
    else:
        print(no2,"is greater")

chkGreater()

# 3) Write a program which accepts one number and prints square of that number
def square(no):
    return no**2

def main():
    num = int(input("Enter number :"))
    ret = square(num)
    print("Square of the above number is :",ret)

if __name__ == "__main__":
    main()


# 4) Write a program which accepts one number and prints cube of that number
def square(no):
    return no**3

def main():
    num = int(input("Enter number :"))
    ret = square(num)
    print("Square of the above number is :",ret)

if __name__ == "__main__":
    main()


# 5) Write a program which accepts one number and checks whether it is divisible by 3 and 5
def checking(no):
    return (no % 3 == 0 and no % 5 == 0)

def main():
    num = int(input("Enter number :"))
    ret = checking(num)

    if ret == True:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")

if __name__ == "__main__":
    main()