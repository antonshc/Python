def gcd(A,B):
	initialA=A
	initialB=B
	while True:
		if A > B:
			A = A - B
		else:
			B = B - A
		if A == B:
			print("GCD of",initialA,"and",initialB,"is:",A)
			break

A = int(input("Enter the first number: \n"))
B = int(input("Enter the second number: \n"))
gcd(A,B)