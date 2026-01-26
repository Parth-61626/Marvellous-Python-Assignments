# Write a program which accept one number and displays below pattern 
# I/P : 3
# output : ***
#          **
#          *

def pattern(num):
    for i in range(num,0,-1):
        print(i * "*")

def main():
    num = int(input("Enter a number :"))
    pattern(num)

if __name__ == "__main__":
    main()