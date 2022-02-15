a = int(input("Enter A: "))
b = int(input("Enter B: "))

product = 1
product2 = 1
for i in range(0, a+1):
    product *= i
    print(i)

for i in range(0, b+1):
    product2 *= i
    print(i)

