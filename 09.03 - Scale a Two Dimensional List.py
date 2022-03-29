def print_list(a):
    for row in a:
        for element in row:
            print(element, end=' ')
        print()

def scale_list(a,s):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j]=s*a[i][j]
            return a

x = open( "09.03 NumbersList.txt", "r" )
a = []

for line in x:
    num = line.split()
    numbers = [int(n) for n in num]
    a.append(numbers)

print_list(a)
s=int(input("Enter the scalar value : "))
a=scale_list(a,s)
print_list(a)