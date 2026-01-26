# Write a program which accept one number from user and return addition of digits in that number

def add(no):
    ans = 0

    while no > 0:
        ans = ans + no % 10
        no = no // 10
    
    return ans

def main():
    no = int(input("Enter a number :"))
    ret = add(no)
    print("Addition of digits is",ret)

if __name__ == "__main__":
    main()