def row(size):
    first=[]
    for i in range(size):
        if i==0 or i==size-1:
            first.append('+')
        else:
            first.append('-')
    return first        
        
x = int(input("Enter Size: "))
size=x + 2
l=[]

l.append(row(size))

for i in range(1,size-1):
    column=[]                
    for j in range(size):
        if j==0 or j==size-1:
            column.append('|')
        else:
            if(i%2==0):
                if(j%2==0):
                    column.append(' ')
                else:
                    column.append('*')
            else:
                if(j%2==0):
                    column.append('*')
                else:
                    column.append(' ')   
                    
    l.append(column)
l.append(row(size))  

y= ""
for i in range(size):
    y+=''.join(l[i])        
    y+='\n'                 
print(y)