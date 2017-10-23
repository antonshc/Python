def pattern(input_number):
	for i in range(input_number+1):
		print(end = "\n")
		for j in range(i):
			print(i, end = "")
	print(end = " \n")
input_number = int(input("Enter a number:\n"))
pattern(input_number)

# Alternative
#num = int(input("Enter number:" ))
#for i in range(num+1):
#    print(i* str(i))
