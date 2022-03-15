x = input("Enter values separated by spaces: ").split()


for i in range(0, len(x), 2):
    if i+1 < len(x):
        x[i], x[i+1] = x[i+1], x[i]

print("Swapped Values: ", end='')
for j in x:
    print(j, end=' ')