while True:
	print("Enter your choice:")
	print("1)Square a number")
	print("2)Area of a triangle")
	print("3)Area of a circle")
	print("4)Area of rectangle")
	print("5)Quit")
	choice = input()
	if choice == '1':
		print ("Enter the number: ")
		square = lambda num: int(num)**2
		print ("square of entered number: ",square(input()))
		continue
	elif choice == '2':
		print ("Enter the base and height of triangle: base height ")
		area = lambda base,height :(base * height)/2
		base,height = input().split()
		print ("Area of a triangle:",area(int(base),int(height)))
		continue
	elif choice == '3':
		print ("Enter the radius of circle: ")
		area = lambda num: 3.14*int(num)**2
		print ("Area of a circle: ",area(input()))
		continue
	elif choice == '4':
		print("Enter the length and width of a rectangle: length width")
		area = lambda width,length :(width * length)
		width,length = input().split()
		print("Area of a rectangle is:",area(int(width),int(length)))
		continue
	else:
		break
