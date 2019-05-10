import sympy
import numpy as np
import random



def shorfactor(n, seed=None):
    random.seed(seed)
    keepgoing = True
    guess1 = None
    guess2 = None
    while(keepgoing):
        g = random.randint(2,n-1)
        print("g is ",g)
        common_den = np.gcd(g,n)
        if(common_den!=1):
            print("g shares a factor with n, breaking out")
            return common_den, n//common_den
        p = findp(n,g)
        print("p is %d"%p)
        findpQuantum(n,g)
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



def superpositionPow(g,sp,modulo=None):
    result = []
    for elem in sp.values:
        result.append((elem,pow(g,elem,modulo)))
    return superPosition(result)



class superPosition():
    def __init__(self,values):
        self.values = values
    def __str__(self):
        return str(self.values)
    def  collapseSuperposition(self):
        return self.values[random.randint(0,len(self.values)-1)]
    def collapseTupleSuperPosition(self):
        ran = random.randint(0,len(self.values)-1)
        power, r = self.values[ran]
        newvals = []
        for elem in self.values:
            if r ==elem[1]:
                newvals.append(elem)
        return superPosition(newvals)






def generaterangeSuperPosition(n):
    values = list(range(1,n+1))
    return superPosition(values)

def findpQuantum(n,g):
    print("shadowing quantum")
    powerpos = generaterangeSuperPosition(n)
    raisedpows = superpositionPow(g,powerpos,modulo=n)
    print("raised pows",raisedpows)



# print(shorfactor(55))
# a = superPosition([55,44])
# print(a.collapseSuperposition())