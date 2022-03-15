x = input("Enter values seprated by spaces: ")

list = x.split()

list = [int(i) for i in list]
l = len(list)

for i in range(l-1):
    if list[i] > 0 and list[i+1] > 0:
        print(list[i], list[i+1])
    elif list[i] < 0 and list[i+1] < 0:
        print(list[i], list[i+1])