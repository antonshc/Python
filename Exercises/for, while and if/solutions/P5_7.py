def pattern(input_number):
	for i in range(1, input_number+1):
	    if i == 1 or i == input_number:
	        print('+' * 7)
	    else:
	        print('+','*' * 5, '+', sep='')

input_number = int(input("Enter a number:\n"))
pattern(input_number)