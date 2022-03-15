x = input("Enter Values Seperated by Spaces in ascending order: ")

list = x.split()

unique = len(set(list))

print("Number of Distinct Elements: ", unique)