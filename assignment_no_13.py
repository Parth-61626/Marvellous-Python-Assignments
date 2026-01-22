# 1) Write a program which accepts length and width of rectangle and prints area

def RectangleArea(length,width):
    area = length * width
    return area

def main1():
    print("Enter length :")
    length = int(input())
    print("Enter width :")
    width = int(input())

    ans = RectangleArea(length,width)
    print("Area of Rectangle is :",ans)

if __name__ == "__main__":
    main1()


# 2)  Write a program which accepts radius of a circle and prints area of the circle

import math

def CircleArea(radius):
    area = math.pi * (radius ** 2)
    return area

def main2():

    print("Enter radius :")
    radius = int(input())

    ans = CircleArea(radius)
    print("Radius of circle is :",ans)

if __name__ == "__main__":
    main2()


# 3) Write a program which accepts one number and checks whether it is perfect number or not

num = int(input("Enter Number :"))

sum = 0

for i in range(1,int(num/2)+1):
    if num % i == 0:
        sum = sum + i

if num == sum:
    print("Number is perfect")


# 4) Write a program which accepts one number and prints binary equivalent

number = int(input("Enter a number :"))

binary_number = ""

while number >= 1:
    binary_number = binary_number + str(number % 2)
    number = int(number / 2)

binary_number = binary_number[::-1]
print("Equivalent binary number is :",binary_number)


# 5) Write a program which accepts marks and displays grade

def grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"
    
def main3():
    marks = int(input("Enter student marks :"))

    Grade = grade(marks)

    print("Grade is :",Grade)

if __name__ == "__main__":
    main3()