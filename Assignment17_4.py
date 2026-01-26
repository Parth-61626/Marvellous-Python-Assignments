# Write a program which accept one number from user and returns addition of its factors

def add(num):
    addition = 0
    for i in range(1,int(num/2)+1):
        if num % i == 0:
            addition = addition + i

    return addition

def main():
    num = int(input("Enter a number :"))
    ret = add(num)
    print("Addition of factors is :",ret)

if __name__ == "__main__":
    main()