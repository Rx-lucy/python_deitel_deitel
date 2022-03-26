import math

total = 0
product = 1
smallest = math.inf
largest = -math.inf

for i in range(4):
    print("Kindly input the number")
    number = int(input())
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

    total = total + number
    product = product * number

average = total / 4

print("Total is = ", total)
print("Average is = ", average)
print("The products is ", product)
print("The highest number is ", largest)
print("The lowest number is ", smallest)