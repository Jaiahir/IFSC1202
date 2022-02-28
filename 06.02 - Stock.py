file = open("06.02 Stock.txt", "r")

x = file.read()

x = [float(i) for i in x.split()]


print("Price      Change")
print (x[0])

for i in range(1, len(x)):
    percent = ((x[i] - x[i-1])/x[i-1]) *100
    print ("{:.2f}    {:+.2f}%".format(x[i], percent))