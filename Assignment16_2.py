# Write a program which contains one function named as ChkNum() which accepts one parameter as number.If number is even it should display "Even number" otherwise display "Odd number on console"

def ChkNum(no):
    return no % 2 == 0

def main():
    num = int(input("enter a number :"))

    result = ChkNum(num)

    if result == True:
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()