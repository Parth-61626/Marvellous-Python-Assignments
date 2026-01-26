# Write a program which accept one number from user and checks if number is prime or not

def chkPrime(num):

    data = []

    for i in range(1,num+1):
        if num % i == 0:
            data.append(i)

    if len(data) == 2:
        print("Prime Number")

def main():
    number = int(input("Enter a number :"))
    chkPrime(number)

if __name__ == "__main__":
    main()