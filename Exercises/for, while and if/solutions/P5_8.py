def pattern(input_number):
    for i in range(1, input_number+1):
        if i == 1 or i == input_number:
            for k in range(1,8):
                if k % 2 == 1:
                    print('+', end='')
                else:
                    print('-',end='')
            print()
        else:
            if i % 2 == 0:
                print('-','*' * 5,'+',sep='')
            else:
                print('+','*' * 5,'-', sep='')

input_number = int(input("Enter a number:\n"))
pattern(input_number)