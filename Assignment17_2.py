# Write a program which accept one number and display below pattern
# Input - 2
# Output - * *
#          * *

def pattern(number):
    for i in range(number):
        print(number * "*")

def main():
    number = int(input("Enter a number :"))
    pattern(number)

if __name__ == "__main__":
    main()