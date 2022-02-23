file = open("06.01 Radius.txt", "r")
r = file.readlines()

def diameter(r):
    for i in range(r):
        return 2 * r

#def circumference(r):
    return 2 * 3.14 * str(r)

#def area(r):
    return 3.14 * str(r*r)



diameter = diameter(r)
#circumference = circumference(r)
#area = area(r)

print (diameter)



