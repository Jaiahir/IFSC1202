x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if x < y < z:
    print (x, y, z)
elif x < z < y:
    print (x, z, y)
elif y < x < z:
    print (y, x, z)
elif y < z < x:
    print (y, z, x)
elif z < x < y:
    print (z, x, y)
elif z < y < x:
    print (z, y, x)