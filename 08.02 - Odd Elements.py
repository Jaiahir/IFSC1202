x = input("Enter Values Separated by Space: ")

list = x.split(" ")

for x in range(len(list)):
    if int(list[x]) % 2 == 1:
        print(list[x])