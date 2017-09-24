#!/usr/bin/python 

#opening a file to read the contents of file.
with open("word.txt") as infile:

	no_of_lines = 0 #variable to hold lines present in file.
	no_of_words = 0 #variable to hold words present in file.
	no_of_characters = 0 #variable to hold character present in file.

	for line in infile:
		words_list = line.split() #spliting the line with respect to space between words.
		no_of_lines = no_of_lines + 1
		no_of_words = no_of_words + len(words_list)
		no_of_characters = no_of_characters + sum(len(word) for word in words_list)

print("no of characters in file",no_of_characters)
print("no of words in a file",no_of_words)
print("no of lines in file",no_of_lines)
