total_miles_per_gallon = 0
count = 0
gallon_used = int(input("Enter the gallon used (Press -1 to end)\n"))

while gallon_used != -1:
    miles_driven = int(input("Kindly enter the miles driven : "))
    miles_per_gallon = miles_driven / gallon_used
    print(f'The miles/gallons for this tank was {miles_per_gallon}')
    total_miles_per_gallon = total_miles_per_gallon + miles_per_gallon
    count +=1
    gallon_used = int(input("Enter the gallon used (Press -1 to end)\n"))

average_total_miles_per_gallon = total_miles_per_gallon / count
print(f'The overall average miles/gallon was {average_total_miles_per_gallon}')

