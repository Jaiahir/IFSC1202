file = open('09.06 CityTemps.txt', 'r')
list = []
list = file.readlines()

header = ["City ","Mo","Tu","We","Th","Fr","Sa","Su","Avg"]

for i in header:
    print(i, end=" ")
print()

for line in list:
    data = line.strip('\n').split(" ")
    total = 0
    for i in data:
        if i.isdigit():
            total = total + int(i)
        print(i, end=" ")
    average = total/7
    print(int(average),end=" ")
    print()