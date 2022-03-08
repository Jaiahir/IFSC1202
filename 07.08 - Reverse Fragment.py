x = str(input("Enter a string with 2 h: "))
h = x[:x.find("h") + 1]
bh = x[x.rfind("h"):]
ch = x[x.find("h")+1:x.rfind("h")]

if x.count("h") >= 2:
  print(h + ch[::-1] + bh)
else:
  print(x.count("h"))