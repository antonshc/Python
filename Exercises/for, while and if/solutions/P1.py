def divisors(input_number):
	a = 0
	b = []
	for i in range(1,input_number+1):
		if input_number % i == 0:
			a = a + 1
			b.insert(i,i)
			# print(i)
	if a == 2:
		print(input_number, "is a prime number.")
	else:
		print(input_number, "is not a prime number")
	print("Divisors of", str(input_number) + ":", b)
input_number = int(input("Enter an integer:\n"))
divisors(input_number)