import sympy
import numpy as np
import random


print(np.__version__)
print("hi")

def shorfactor(n):
    keepgoing = True
    guess1 = None
    guess2 = None
    random.seed(3)
    while(keepgoing):
        g = random.randint(2,n-1)
        print("g is ",g)
        common_den = np.gcd(g,n)
        if(common_den!=1):
            print("g shares a factor with n, breaking out")
            return common_den, n//common_den
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
    return (factor1, n//factor1)


def findp(n,g):
    for i in range(1,n):
        raisedpow = g**i
        remainder = raisedpow % n
        if (remainder ==1):
            return i



class superPosition():
    def __init__(self,values):
        self.values = values

    def  collapseSuperposition(self):
        return self.values[random.randint(0,len(self.values)-1)]




print(shorfactor(55))
a = superPosition([55,44])
print(a.collapseSuperposition())