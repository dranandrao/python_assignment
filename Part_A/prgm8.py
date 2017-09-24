#!/usr/bin/python
from cmath import sqrt #importing sqrt function.
print("Enter the values of the eqauation")

#get values of quadratic equation.
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

#calculate the roots.
roots_of_equation = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)

print("solution for quadratic equation is ",roots_of_equation) 
