# Create a module named as Arithmetic which contains four functions as Add() for addition,
# Sub() for subtraction,Mult() for multiplication and Div() for division.All functions 
# accepts two parameters as number and perform the operation.Write a python program which
# call all the functions from arithmetic module by accepting the parameter from user

import Arithmetic

Addition = Arithmetic.Add(20,10)
Subtraction = Arithmetic.Sub(20,10)
Multiplication = Arithmetic.Mult(20,10)
Division = Arithmetic.Div(20,10)

print("Addition is :",Addition)
print("Subtraction is :",Subtraction)
print("Multiplication is :",Multiplication)
print("Division is :",Division)