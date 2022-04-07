class Pet:
    def __init__(self):
        self.Name = ""
        self.Type = ""
        self.Age = 0

    def __repr__(self):
        return "{0}\t{1}\t{2}".format(self.Name,self.Type,self.Age)

pet1 = Pet()
pet2 = Pet()
pet3 = Pet()

with open("10.01 Pets.txt","r") as file:
    data = file.readline()
    rowData = data.strip().split(' ')
    pet1.Name = rowData[0]
    pet1.Type = rowData[1]
    pet1.Age = rowData[2]

    data = file.readline()
    rowData = data.strip().split(' ')

    pet2.Name = rowData[0]
    pet2.Type = rowData[1]
    pet2.Age = rowData[2]

    data = file.readline()
    rowData = data.strip().split(' ')

    pet3.Name = rowData[0]
    pet3.Type = rowData[1]
    pet3.Age = rowData[2]

print("Name\tType\tAge")

print (pet1)
print (pet2)
print (pet3)