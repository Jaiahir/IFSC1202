x = float(input("Enter length of km in a race: "))
y = float(input("Number of minutes required: "))
z = float(input("Number of seconds required: "))

miles = float(x/1.61)

mininsec = y * 60

totaltimeinsec = mininsec + z

hours = totaltimeinsec/3600

milesperhour = miles/hours

print (milesperhour)