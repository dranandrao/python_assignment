#!/usr/bin/python

#Get vertices of traingle.
print("Enter the vertices X1 and Y1")
x1 = float(input("X1"))
y1 = float(input("Y1"))

print("Enter the vertices X2 and Y2")
x2 = float(input("X2"))
y2 = float(input("Y2"))

print("Enter the vertices X3 and Y3")
x3 = float(input("X3"))
y3 = float(input("Y3"))

#calculting the centroid of traingle.
cx1 = (x1+x2+x3)/3
cy1 = (y1+y2+y3)/3

print("Centroid of traingle is ",cx1,cy1)
