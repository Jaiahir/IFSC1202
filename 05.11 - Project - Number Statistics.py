count = 0
sum = 0
min = 0
max = 0

num = int(input(("Enter a value (Zero to quit): "))

while num != 0:
    sum += num    
    average = sum / num
    num = int(input(("Enter a value (Zero to quit): "))

if (num > max): 
    max = num;

if (num < min):
    min = num


print("Your average is: " + average)
print("The sum is: " + sum)  
print("Your maximum number is: " + max)
print("Your minimum number is: " + min)