def isEven(num):
    return num%2==0

def isOdd(num):
    return num%2==1

def isPrime(num):
    if num<0:return False
    if num==2 or num==3: return True
    if num%2==0 or num<2: return False
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            return False
    return True

def main():
    filename="06.06 Numbers.txt"
    evens=[]
    odds=[]
    primes=[]
    with open(filename,'r') as infile:
        for line in infile:
            num = int(line.strip())
            if isEven(num):evens.append(num)
            elif isOdd(num):odds.append(num)
            if isPrime(num):primes.append(num)

    with open("06.06 Evennumbers.txt",'w+') as outfile:
        for num in evens:
            outfile.write('{}\n'.format(num))

    with open("06.06 Evennumbers.txt", 'w+') as outfile:
        for num in odds:
            outfile.write('{}\n'.format(num))
    with open("06.06 Primenumbers.txt", 'w+') as outfile:
        for num in primes:
            outfile.write('{}\n'.format(num))
    print('{} even numbers'.format(len(evens)))
    print('{} odd numbers'.format(len(odds)))
    print('{} prime numbers'.format(len(primes)))
    print('{} numbers read'.format(len(evens)+len(odds)))
main()