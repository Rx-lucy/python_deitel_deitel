number = int(input('Input numbers, press -1 to stop\n'))
while number != -1:
    num1 = number // 10000
    num2 = (number // 1000) % 10
    num3 = (number // 100) % 10
    num4 = (number % 100) // 10
    num5 = number % 10
    print(num1, "   ", num2, "   ", num3, "   ", num4, "   ", num5)
    number = int(input('Input numbers, press -1 to stop \n'))
