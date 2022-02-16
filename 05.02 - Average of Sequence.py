x = int(input("Enter a Number (zero to quit): "))
sum = x


while x != 0:
    avg = sum / x
    x = int(input("Enter a Number (zero to quit): "))
else:
    print('Average: ' + str(avg))