""" Assuming that the angle to top of tree is taken with respect to ground level and not with respect to person eye."""
import math

distance = float(input("Enter the distance to the tree"))

if distance < 0:
	print("Distance should be a positive number")

angle = float(input("Enter the angle"))

if angle < 0 and angle > 90:
	print("Angle should be positive number less than 90 degree")

#converting degree to radian,and calculating tangent.
print("height of the tree is ",(math.tan(math.radians(angle))*distance))
