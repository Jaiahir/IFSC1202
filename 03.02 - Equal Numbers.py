x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if x == y == z:
    print ("3")
elif x == y:
    print ("2")
elif x == z:
    print ("2")
elif y == x:
    print ("2")
elif y == z:
    print ("2")
elif z == x:
    print ("2")
elif z == y:
    print ("2")
else:
    print ("0")