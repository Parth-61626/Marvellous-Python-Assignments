# Write a program which contains one function that accept one number from user and return true if number is divisible by 5 otherwise false

def chk_div(no):
    return no % 5 == 0

def main():
    num = int(input("Enter a number :"))

    result = chk_div(num)
    print(result)

if __name__ == "__main__":
    main()