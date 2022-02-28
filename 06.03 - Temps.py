def FahrToCel():
    f = float(input())
    c = (f-32) * 5/9
    return

file = open("06.03 FTemps.txt", "r")
file = open("06.03 FTemps.txt", "w")

recordcount = 0
list = []

while True:
    line = file.readline()
    if not line:
        break
    else:
        list.append(float(line))

for f in list:
        print()