num = int(input("Enter a value (Zero to quit): "))
count = 0
sum = 0
min = num
max = num

while num > 0:
    sum += num
    count += 1
    if num > max:
        max = num

    if num < min:
        min = num 
    num = int(input("Enter a value (Zero to quit): "))


print("Your count is: " + str(count))
print("The sum is: " + str(sum))
print("Your average is: " + str(sum/count))
print("Your minimum number is: " + str(min))
print("Your maximum number is: " + str(max))