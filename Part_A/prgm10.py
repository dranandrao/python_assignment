#!/usr/bin/python

#creating a dictionary
fruits = {"orange":1,
	"apple" : 2,
	"Watermelon":3,
	"Mosumbi":4,
	"Jackfruit":5,
	"grapes":6
	}

#checking condition fruit not equal to orange and apple
for key in fruits.keys():
	if key != 'orange' and key != 'apple':
		fruits.pop(key)

print(fruits.items())
