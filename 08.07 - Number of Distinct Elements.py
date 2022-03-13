inp = raw_input("Enter values separated by spaces\n")

li = list(inp.split(" "))

n=len(li)

def Distinct(li,n):
    res=1
for i in range(1,n):
    k=0
for k in range(i):
   if (li[i] == li [k]):
     break
   if (i == k+1):
     res+=1
return res


print("Number of Distinct elements: ")
print(Distinct(li,n,))