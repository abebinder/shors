import random

def isPrime(num):
    if num <= 2:
        return False
    if num % 2 == 0:
        return False
    for possibleFactor in range(3, int(pow(num, .5)) + 2, 2):
        if num % possibleFactor == 0:
            return False
    return True

def getPrime(num_bits):
    startNum = 2 ** num_bits
    endNum = 2 ** (num_bits+1)
    while True:
        randomNum = random.randint(startNum, endNum)
        if isPrime(randomNum):
            return randomNum

def findGCDRecursive(one, two):
    if two == 0:
        return one
    return findGCDRecursive(two, one % two)

def getRandomWithLower(lower, upper):
    return random.randint(lower, upper)

def getRandom(less):
    return random.randint(1,less)

def getN(bits):
        prime = getPrime(bits)
        prime2 = getPrime(bits)
        while prime == prime2:
            prime2 = getPrime(bits)
        N = prime * prime2
        print("Prime is %d" % prime)
        print("Prime2 is %d" % prime2)
        print("N is %d" % N)
        return N
def computeGCD(x, y):

   while(y):
       x, y = y, x % y

   return x
