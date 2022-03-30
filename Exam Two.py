file = open("CarSales.txt","r")

list = []

for line in file:
        line=line.replace("\n","")
        line=line.split(",")
        list.append(line)
file.close()

carnum = 0
total = 0

for car in list:
        carnum +=1
        total+=float(car[1]) 
        avg = total/carnum
print(carnum, "Total Cars")
print("Average Price: $",round(avg))    

x = input("Enter Car Make: ")
while(x != ""):
        cars = 0
        price = 0
        for car in list:
                if car[0]==x:
                        cars+=1 
                        price+=float(car[1])
        if(cars != 0):
                avgx = price/cars
                print(cars, "Cars Sold")
                print("$",round(avgx), " Average Price")
                difference = avgx-avg    
                percent = (difference*100)/avg
                print(round(percent,2), "% Above/Below Average")
        else:
                print("Car Make Not Found")
        x = input("Enter Car Make: ")