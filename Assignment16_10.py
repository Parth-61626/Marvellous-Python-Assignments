# Write a program which accepts name from user and display length of its name

def length(name):
    print("length of name is :",len(name))

def main():
    name = input("enter name :")
    length(name)

if __name__ == "__main__":
    main()