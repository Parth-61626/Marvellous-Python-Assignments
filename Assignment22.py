# 1)

class Demo:

    value = 0

    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("Value of no1 is :",self.no1)
        print("Value of no2 is :",self.no2)

    def Gun(self):
        print("Value of no1 is :",self.no1)
        print("Value of no2 is :",self.no2)


Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()


# 2)

class Circle:
    
     PI = 3.14

     def __init__(self):
         self.Radius = 0.0
         self.Area = 0.0
         self.Circumference = 0.0


     def Accept(self):
         self.Radius = float(input("Enter radius :")) 
     
     def CalculateArea(self):
         self.Area = Circle.PI * self.Radius * self.Radius
     
     def CalculateCircumference(self):
         self.Circumference = 2 * Circle.PI * self.Radius
     
     def Display(self):
         print("Radius :",self.Radius)
         print("Area :",self.Area)
         print("Circumference :",self.Circumference)

Obj1 = Circle()
Obj2 = Circle()
Obj3 = Circle()

Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()

Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
Obj2.Display()

Obj3.Accept()
Obj3.CalculateArea()
Obj3.CalculateCircumference()
Obj3.Display()


# 3)

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter a number :"))
        self.Value2 = float(input("Enter a number :"))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        return self.Value1 / self.Value2


obj1 = Arithmetic()
obj2 = Arithmetic()

obj1.Accept()
obj1.Addition()
obj1.Subtraction()
obj1.Multiplication()
obj1.Division

obj2.Accept()
obj2.Addition()
obj2.Subtraction()
obj2.Multiplication()
obj2.Division()