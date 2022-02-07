x = float(input("Enter a positive real number: "))

dec = (x%1) * 100
oned = dec//10

print("{}".format(int(oned)))