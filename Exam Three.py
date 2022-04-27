class House:
   def __init__(self, address, sqft, price):
       self.address = address
       self.sqft = sqft
       self.price = price

   def costpersqft(self):
       return self.price / self.sqft

#tried it but I was getting typerror: float object not callable
   def payment(self, ar, ny):
       #interest = ar / 1200
       #months = ny * 12
       #payment = self.price (interest (1 + interest) ** months) / ((1 + interest) ** months - 1)
       return 100

HouseList = []

file = open("Exam Three Houses.txt", "r")

for line in file:
   data = line.split(',')
   address = data[0]
   sqft = int(data[1])
   price = int(data[2])

   house = House(address, sqft, price)
   HouseList.append(house)

interest = int(input("Enter Interest Rate: "))
interest = interest / 100

mortage = int(input("Enter Years For Mortage: "))

print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}\n".format("Address", "Sq Ft", "SqFt Cost", "Price", "Payment"))

for house in HouseList:
   print("{0:<15}{1:<15}{2:<15.2f}{3:<15.2f}{4:<15.2f}"
       .format(house.address, house.sqft, house.costpersqft(), house.price, house.payment(interest, mortage)))