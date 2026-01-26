# Write a program which accept one number and displays below pattern 
# I/P : 3
# output : 1
#          12
#          123

def pattern(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end = "")
        print()

def main():
    num = int(input("Enter a number :"))
    pattern(num)

if __name__ == "__main__":
    main()