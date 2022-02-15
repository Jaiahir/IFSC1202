n = int(input("Enter N: "))

if n > 1:
    for i in range(2, int(n/2)+1):
        if (n % i) == 0:
            print("Composite")
            break
    else:
        print("Prime")
else:
    print("Composite")