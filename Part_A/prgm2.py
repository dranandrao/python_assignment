#!/usr/bin/python

print("Enter the height of a triangle")

#Get height of triangle.
height = float(input("height :"))

#checking for negetive and zero conditions.
if height <= 0:
	print("Height cannot be negetive or zero")
print("Enter the base of triangle")

#Get base of triangle.
base = float(input("base: "))
if base <= 0:
	print("base cannot be negetive or zero")

#calculating area of triangle if greater than condition met.
if height > 0 and base > 0:
	area_of_traingle = (height * base)/2

print("The are of a trianle is ",area_of_traingle)
