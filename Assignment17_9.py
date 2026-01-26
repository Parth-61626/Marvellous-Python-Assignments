# Write a program which accept one number from user and return number of digits in that number

def Count(no):
    count = 0

    if no == 0 :
        count = 1
    else:
        while no > 0:
            count = count + 1
            no = no // 10

    return count

def main():
    num = int(input("Enter the number :"))
    ret = Count(num)
    print("Number of digits :",ret)

if __name__ == "__main__":
    main()