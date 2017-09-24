#!/usr/bin/python

#importing square root function from math class.
from math import sqrt
print("Enter the sides of a right angle triangle")

#get sides of the traingle from user.
a = float(input("a: "))
b = float(input("b: "))

#checking for negetive and zero values.
if a <= 0:
    print("value 'a' cannot be negetive or zero")

if b <= 0:
    print("value 'b' cannot be negetive or zero")

 
#calculating hypotenuse.
if a > 0 and b > 0:
    hypotenuse = sqrt(a**2 + b**2)
    print("hypotenuse of right angle traingle is ",hypotenuse)

