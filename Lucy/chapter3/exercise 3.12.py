x = int(input('enter five integer\n'))

x_1 = x // 10000
x_2 = (x // 1000) % 10
x_3 = (x // 100) % 10
x_4 = (x % 100) // 10
x_5 = x % 10

if (str(x)) == (str(x_5) + str(x_4) + str(x_3) + str(x_2) + str(x_1)):
    print('This is a palindrome number')
else:
    print("This is not a palindrome number")
