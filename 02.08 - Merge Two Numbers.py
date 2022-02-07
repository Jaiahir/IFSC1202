x = int(input("Enter a 2 digit number: "))
y = int(input("Enter another 2 digit number: "))

onesd1 = x//10
tensd1 = x % 10

onesd2 = y//10
tensd2 = y % 10

print("{}{}{}{}".format(onesd1, onesd2, tensd1, tensd2))