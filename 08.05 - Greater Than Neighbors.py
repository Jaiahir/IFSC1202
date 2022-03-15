x = [int(l) for l in input("Enter Values Separated by Spaces: ").split()]

output = 0

for i in range(1, len(x)-1):
    if x[i - 1] < x[i] > x[i + 1]:
       output += 1
print(output)