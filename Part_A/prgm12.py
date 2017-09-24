#!/usr/bin/python

input_str = raw_input("Enter the string: ")

#varibles to hold the count of individual vowels occurences.
acount = 0
ecount = 0
icount = 0
ocount = 0
ucount = 0

for char in input_str:
	if char == 'a' or char == 'A':
		acount = acount + 1
	elif char == 'e' or char == 'E':
		ecount = ecount + 1
	elif char == 'i' or char == 'I':
		icount = icount + 1
	elif char == 'o' or char == 'O':
		ocount = ocount + 1
	elif char == 'u' or char == 'U':
		ucount = ucount + 1	

print("vowel counts are ","a:",acount,"e:",ecount,"i:",icount,"o:",ocount,"u:",ucount)

	
