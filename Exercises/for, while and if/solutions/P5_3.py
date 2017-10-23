def pyramid(input_number):
	for i in range(1, input_number+1):
	    if (i % 2) == 0:
	        print(str(i) * i)
	    elif i == 1:
	        print(str(i) * i)
	    else:
	        for k in range(1,i+1):
	            print(i, end='')
	            i -= 1
	        print()

input_number = int(input("Enter a number:\n"))
pyramid(input_number)