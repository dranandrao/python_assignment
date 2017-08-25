#!/usr/bin/python
import getpass

print("Enter the username")
username = raw_input("Username: ")

print("Enter the password")
password = getpass.getpass("Password: ")

print("Username and password recieved ",username,password) 