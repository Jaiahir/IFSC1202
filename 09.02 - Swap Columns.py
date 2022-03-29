def print_list(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
                       print(a[i][j],end=' ')
        print('\n')

def swap_columns(a,i,j):
    for k in range(len(a)):
        l=a[k][i]
        a[k][i]=a[k][j]
        a[k][j]=l

x=open('09.02 NumbersList.txt')
y=x.readlines()
y=''.join(y)
y=y.split('\n')
for i in range(len(y)):
    y[i]=y[i].split(' ')
    y[i]=map(int,y[i])
    y[i]=list(y[i])
print_list(y)

i,j=input('Enter the columns to swap: ').split()
i=int(i)
j=int(j)
swap_columns(y,i,j)
print_list(y)