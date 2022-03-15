x = input("Enter Values Seperated by Spaces: ")
numbers = (list(x.split(" ")))
numbers = [int(numbers[x]) for x in range(len(numbers))]

n = len(numbers)
min = 0
max = 0

for x in range(n):
    if numbers[x] < numbers[min]:
        min = x
    if numbers[x] > numbers[max]:
        max = x

numbers[min], numbers[max] = numbers[max], numbers[min]

print("Swapped Minimum and Maximum:", end=" ")
for i in range(n):
    print(numbers[i], end=" ")