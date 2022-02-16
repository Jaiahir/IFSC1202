x = int(input("Enter a Number (zero to quit): "))
sum = 0
count = 0

while x > 0:
    sum += x
    count +=1
    x = int(input("Enter a Number (zero to quit): "))
else:
    print('Average: ' + str(sum/count))