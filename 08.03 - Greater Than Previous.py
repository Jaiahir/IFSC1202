x = input("Enter Values Separated by Spaces: ")

list = []

for x in x.split(" "):
    list.append(int(x))

for i in range(1, len(list)):
    if list[i] > list[i-1]:
        print(list[i])