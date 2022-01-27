print("First Timestamp")
x1 = input("Enter Hours: ")
y1 = input("Enter Minutes: ")
z1 = input("Enter Seconds: ")

print("Second Timestamp")
x2 = input("Enter Hours: ")
y2 = input("Enter Minutes: ")
z2 = input("Enter Seconds: ")

total1 = int(x1*3600) + int(y1*60) + int(z1)
total2 = int(x2*3600) + int(y2*60) + int(z2)

print(total2-total1)