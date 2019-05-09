import sympy
import numpy as np
import random


print(np.__version__)
print("hi")

def shorfactor(n):
    keepgoing = True
    guess1 = None
    guess2 = None
    while(keepgoing):
        random.seed(3)
        g = random.randint(2,n-1)
        p = findp(n,g)
        guess1 = g**(p//2) + 1
        print(guess1)
        guess2 = g**(p//2) - 1
        print(guess2)
        if(p%2==1):
            continue
        if (guess1%n == 0 ):
            continue
        if(guess2%n == 0 ):
            continue
        keepgoing = False
    factor1 = np.gcd(guess1,n)
    print(factor1, n//factor1)


def findp(n,g):
    for i in range(1,n):
        raisedpow = g**i
        remainder = raisedpow % n
        if (remainder ==1):
            return i



shorfactor(55)
