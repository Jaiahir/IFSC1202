x = input("Enter Values Separated by Spaces: ").split()

for i in range(len(x)):
    x[i] = int(x[i])

print("Unique Elements: ", end="")

for i in range(len(x)):
    count = 0
    for j in range(len(x)):
        if x[i] == x[j]:
            count += 1
    if count == 1:
        print(x[i], end=" ")
print()