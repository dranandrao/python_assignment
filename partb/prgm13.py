import sys,getopt
import re

inputs = ('')
no_of_occurance = 0
try:
	opts ,args = getopt.getopt(sys.argv[1:],'i:o:')
except getopt.GetoptError as error:
	print ("Error")
	print ("usage <filename.py> -i <input> -o <output>")#priting the usage cases.
	print str(error)

match_string = input("Enter the string to matched: ")

for inpt,oupt in opts:
	if inpt == "-i":
		f = open(oupt,"r")
		data = f.readline()#reading the file line by line.
		while data != '':
			result = re.search(match_string,data)
			if result:
				no_of_occurance = no_of_occurance + 1
			data = f.readline()

	elif inpt == "-o":
		f = open(oupt,"w")
		f.write("no of occurance of"+ ' ' + str(match_string) + '\t' + str(no_of_occurance))#writing the data to the file.
		f.close()
