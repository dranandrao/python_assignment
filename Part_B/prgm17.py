def find_no_lines(infile):
	infile.seek(0)#bringing the pointer back to first position.
	no_of_lines = 0
	for line in infile:
		words_list = line.split()
		no_of_lines = no_of_lines + 1
	print("no of lines in file",no_of_lines)
		
def find_no_words(infile):
	infile.seek(0))#bringing the pointer back to first position.
	no_of_words = 0
	for line in infile:
		words_list = line.split()
		no_of_words = no_of_words + len(words_list)
	print("no of words in file",no_of_words)

def find_no_characters(infile):
	infile.seek(0))#bringing the pointer back to first position.
	no_of_characters = 0
	for line in infile:
		words_list = line.split()
		no_of_characters = no_of_characters + sum(len(word) for word in words_list)
	print("no of characters in file",no_of_characters)

def main():
	with open("word.txt") as infile:
		find_no_lines(infile)
		find_no_words(infile)
		find_no_characters(infile)
	
if __name__ == "__main__":
	main()
