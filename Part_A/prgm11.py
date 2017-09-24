#!/usr/bin/python
number = int(input("Enter the number: "))

#method to check if number is amstrong.
def checkIfAmstrong(number):
	sum_of_numbers = 0
	temp = number
	while temp > 0:
		digit = temp % 10 #get last digit of given number.
		sum_of_numbers = sum_of_numbers + (digit**3)
		temp = temp/10

	if number == sum_of_numbers:
		return True
	else:
		return False

#Method to check if number is prime.
def  checkIfPrime(number):
	if number > 1:
		for i in range (2,number):
			if(number % i) == 0:
				return False

		return True
	else:
		return False

is_prime = checkIfPrime(number)
is_amstrong = checkIfAmstrong(number)


if(is_prime == True and is_amstrong == True):
	print("Number is both prime and Amstrong number")
elif (is_prime == True and is_amstrong == False):
	print("number is prime number and not Amstrong number") 
elif (is_amstrong == True and is_prime == False):
	print("number is Amstrong number and not a prime number ")
else:
	print("number is not amstrong number nor a prime number")
