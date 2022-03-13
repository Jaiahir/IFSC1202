x = input("Enter Values Separated by Space: ")

n = x.split(" ")
list = []

for num in n:
    list.append(num)

for x in range(len(list)):
    if x % 2 != 0:
        print(list[x])