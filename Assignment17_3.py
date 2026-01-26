# Write a program which accept one number from user and returns its factorial

def fact(number):
    factorial = 1
    for i in range(1,number+1):
        factorial = factorial * i

    return factorial

def main():
    num = int(input("Enter a number :"))
    ret = fact(num)
    print("Factorial is :",ret)

if __name__ == "__main__":
    main()