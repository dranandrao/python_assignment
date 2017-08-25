#!/usr/bin/python
import getpass

users = {}

for x in range(5):
	print("Enter username",x)
	username = raw_input("Username: ")
	print("Enter password")
	password = getpass.getpass("Password :")
	
	#storing password into Dictionary.
	users[username] = password

print(users)
