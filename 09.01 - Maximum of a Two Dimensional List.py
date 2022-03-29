print("Enter the number of rows and columns: ")
m = int(input())
n = int(input())
#Enter each number one by one and press enter after each number including the list values

list = []

for i in range(m):          
    l = []
    print("Enter a line of data:")
    for j in range(n):      
        l.append(int(input()))
    list.append(l)
 
for i in range(m):          
    for j in range(n):      
        print(list[i][j],end = " ")
    print()

max = 0
for i in range(m):          
    for j in range(n):  
        if max < list[i][j]:
            max = list[i][j]

a = 0
b = 0
for i in range(m):          
    for j in range(n):  
        if max == list[i][j]:
            a = i
            b = j
            print("The maximum value",max,"occurred in row",a,"column",b)
            break