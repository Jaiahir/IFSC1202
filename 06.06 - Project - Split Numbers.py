def isEven(x):
    return x % 2 == 0

def isOdd(x):
    return x % 2 == 1

def isPrime(x):
    if x < 0: return False
    if x == 2 or x == 3: return True
    if x % 2 == 0 or x < 2: return False
    for i in range(3, int(x**0.5) + 1,2):
        if x % i == 0:
            return False
    return True

def mainOutput():
    file = "06.06 Numbers.txt"
    evens=[]
    odds=[]
    primes=[]
    with open(file,"r") as infile:
        for line in infile:
            x = int(line.strip())
            if isEven(x):evens.append(x)
            elif isOdd(x):odds.append(x)
            if isPrime(x):primes.append(x)

    with open("06.06 Evennumbers.txt",'w+') as file0:
        for x in evens:
            file0.write("{}\n".format(x))
    with open("06.06 Evennumbers.txt", 'w+') as file0:
        for x in odds:
            file0.write("{}\n".format(x))
    with open("06.06 Primenumbers.txt", 'w+') as file0:
        for x in primes:
            file0.write("{}\n".format(x))

    print(len(evens), "even numbers")
    print(len(odds), "odd numbers")
    print(len(primes), "prime numbers")
    print(len(evens)+len(odds), "numbers read")
mainOutput()