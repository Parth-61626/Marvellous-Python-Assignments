# Write a program which accept one number and displays below pattern 
# I/P : 3
# output : 123
#          123
#          123

def pattern(num):
    for i in range(num):
        for j in range(1,num+1):
            print(j,end = "")
        print()

def main():
    num = int(input("Enter a number :"))
    pattern(num)

if __name__ == "__main__":
    main()