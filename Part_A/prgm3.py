#!/usr/bin/python
from math import sqrt
 
print("Enter the vertices of two points")

#Get vertices of points.
x1 = input("x1: ")
y1 = input("y1: ")
x2 = input("x2: ")
y2 = input("y2: ")

euclidian_distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("euclidian distance is:",euclidian_distance)
