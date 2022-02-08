a = int(input("Enter point A: "))
b = int(input("Enter point B: "))
c = int(input("Enter point C: "))

distanceAB = b - a
distanceAC = c - a


if b == a:
    print(distanceAB)
elif c == a:
    print(distanceAC)
elif distanceAB < distanceAC:
    print(abs(distanceAB))
elif distanceAC < distanceAB:
    print(abs(distanceAC))