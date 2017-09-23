import argparse,sys
import re

no_of_occurance = 0#count of a word.

parser = argparse.ArgumentParser()
parser.add_argument('-i','--input',required=True)
parser.add_argument('-o','--output',required=True)
args = parser.parse_args()

match_string = input("Enter the string to matched: ")
f = open(args.input,"r")
data = f.readline()
while data != '':
	result = re.search(match_string,data)
	if result:
		no_of_occurance = no_of_occurance + 1
	data = f.readline()

f = open(args.output,"w")
f.write("no of occurance of"+ ' ' + str(match_string) + '\t' + str(no_of_occurance))#writing to file.
f.close()
