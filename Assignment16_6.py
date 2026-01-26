# Write a program which accept number from user and check if that number is positive or negative or zero


def chk(num):
    if num > 0:
        print("Positive")
    elif num == 0:
        print("Zero")
    else:
        print("Negative")

def main():
    num = int(input("Enter a number :"))
    chk(num)

if __name__ == "__main__":
    main()