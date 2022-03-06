x = input("Enter a string: ")

for i in range(len(x)//2, len(x)): 
    print(x[i], end="")

for i in range(len(x)//2):
    print(x[i], end="")