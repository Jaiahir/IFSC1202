x = int(input("Enter Year: "))

leap1 = x % 4
leap11 = x % 100
leap2 = x % 400

if leap1 == 0 and leap11 != 0:
    print("Leap Year")
elif leap2 == 0:
    print("Leap Year")
else:
    print("Common Year")

    

