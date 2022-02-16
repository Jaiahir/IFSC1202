from random import randint

name = str(input("Hello! What is your name? "))
print("Well,", name ,"I am thinking of a number between 1 and 20.")
print("You have 5 guesses.")

max = 5
num = randint(1, 20)

for i in range(max):
    g = input("Take a guess: ")
    i = int(g)
    if i == num:
        print('You won!!!')
        break
    elif i > num:
               print("Your guess is too high")
    elif i < num:
               print("Your guess is too low")
    else:
        print("Nope. The number I was thinking of was", num)