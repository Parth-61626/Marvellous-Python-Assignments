# Write a program which accepts number from user and prints that number of "*" on screen


def pattern1(number):
    print(number * "*")

def main():
    number = int(input("Enter a number :"))
    pattern1(number)

if __name__ == "__main__":
    main()

# OR

def pattern2(number):
    for i in range(1,number+1):
        print("*")

def main():
    number = int(input("Enter a number :"))
    pattern2(number)

if __name__ == "__main__":
    main()