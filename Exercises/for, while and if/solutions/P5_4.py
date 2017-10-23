def pyramid(input_number):
	for i in range(1,3):
	    print("*" * i)
	for i in range(1, input_number+1):
	    print("*","-"*i,"*", sep="")
	print("*" * (input_number+3))

input_number = int(input("Enter a number:\n"))
pyramid(input_number)
