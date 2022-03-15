x = input("Enter Values Saparated by Spaces: ")

x = [int(i) for i in x.split()]

index = 0
value = x[0]

for i in range(len(x)):
    if x[i] > value:
        value = x[i]
        index = i

print("Largest Value: ",value)

print("Index of Largest Value: ",index)