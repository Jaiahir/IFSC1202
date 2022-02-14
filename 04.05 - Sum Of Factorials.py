x = int(input("Enter Number: "))


product = 1
sum = 0
for i in range(1, x+1):
    product *= i
    sum += product


print(sum)