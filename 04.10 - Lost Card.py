n = int(input("Enter number of cards: "))

answer=0
n0=n 

for i in range(n-1):
  n=int(input("Enter Card: "))
  answer+=n
for i in range(n0):
  n0 += i
  i += n0
n0 -= answer

print("Missing Card:", n0)