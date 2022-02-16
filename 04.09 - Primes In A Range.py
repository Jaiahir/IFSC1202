a = int(input("Enter A: "))
b = int(input("Enter B: "))


if a > 1 and b > 1:
    for i in range(2, b+1):
        if (b % i) == 0:
            break
        else:
            print(b)




