x = int(input("Enter a 4 digit number: "))

oned = x%10
twod = (x % 100) // 10 
threed = (x%1000) // 100
thoud = x // 1000

first = oned + twod
second = threed + thoud

if oned == thoud and twod == threed:
    print("YES")
else:
    print("NO")