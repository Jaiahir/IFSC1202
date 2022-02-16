x = int(input("Enter a Number (zero to quit): "))
total = 0

while x != 0:
    total += x
    x = int(input("Enter a Number (zero to quit): "))
else:
    print('Sum: ' + str(total))


