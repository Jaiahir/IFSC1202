class RetailItem:
   def __init__(self,Description="",UnitsOnHand=0,Price=0):
       self.Description = Description
       self.UnitsOnHand = UnitsOnHand
       self.Price = Price
   def InventoryValue(self):
       return self.UnitsOnHand * self.Price

items = []
file = open("10.02 Inventory.txt","r")

for line in file:
   words = line.split(",")
   items.append(RetailItem(words[0],float(words[1]),float(words[2])))

print("Description\tUnits On Hand\t\t\t Price \t\tInventory Value")
print(items[0].Description,"\t\t\t",items[0].UnitsOnHand,"\t\t\t ",items[0].Price,"\t\t\t {:.2f}".format(items[0].InventoryValue()))
print(items[1].Description,"\t\t\t",items[1].UnitsOnHand,"\t\t\t",items[1].Price,"\t\t\t{:.2f}".format(items[1].InventoryValue()))
print(items[2].Description,"\t\t\t",items[2].UnitsOnHand,"\t\t\t",items[2].Price,"\t\t\t {:.2f}".format(items[2].InventoryValue()))