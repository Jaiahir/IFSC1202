import math

def diameter(r):
        return 2 * r

def circumference(r):
    return 2 * math.pi * r

def area(r):
    return math.pi * r * r

def main():

    file = open("06.01 Radius.txt","r")

    list = []

    while True:
        line = file.readline()
        if not line:
            break
        else:
            list.append(float(line))

    print("{:>15} {:>15} {:>15} {:>15}".format("Radius","Diameter","Circumference","Area"))
    for r in list:
        print("{:>15.5f} {:>15.5f} {:>15.5f} {:>15.5f}".format(r,diameter(r),circumference(r),area(r)))

if __name__ == "__main__":
    main()


