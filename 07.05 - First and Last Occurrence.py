x = input("Enter a string: ")
fi = -1
li = 0


for i in range(len(x)):
    if x[i] == "f":
        if fi == -1:
            fi = i
        li = i

if fi == li:
    print(fi)
else:
    print(fi, li)