x = int(input("Enter a 3 digit number: "))

oned = x//100
twod = (x % 100) // 10 
threed = x%10

sum = (oned+twod+threed)

print("{}".format(sum))