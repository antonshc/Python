input_number = int(input("Enter a number:\n"))
def pyramid(input_number):
	for i in range(1,input_number+1):
		print('.' * (input_number - i), end='')
		for k in range(1):
			print(str(i) * i)

pyramid(input_number)