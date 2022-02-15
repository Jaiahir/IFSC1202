a = int(input("Enter A: "))
b = int(input("Enter B: "))

product = 1

for i in range(b+1):
    product *= i
    print(i, "*", i, "=", i*i, sep='')

