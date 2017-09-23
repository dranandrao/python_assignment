import wget,os
while True:
	print("1)Download kernel image")
	print("2)Delete kernel image")
	print("3)Quit")
	global filename
	choice = input()
	if choice == 1:
		url = "https://www.kernel.org/pub/linux/kernel/v4.x/stable-review/patch-4.9.8-rc1.gz"
		filename = wget.download(url)
		print("\n File "+filename+" has been downloaded")
		continue
	elif choice == 2:
		os.remove(filename)
		print("File "+filename+" has been deleted")
		continue
	else:
		break



