x = int(input("Enter the first number "))
y = int(input("Enter the second number "))
z = int(input("Enter the third number "))

if x < y:
    print (x)
elif x < z:
    print (x)
elif y < x:
    print (y)
elif y < z:
    print (y)
elif z < x:
    print (z)
elif z < y:
    print (z)