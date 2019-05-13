import sympy
import numpy as np
import random
import util
import time

VERBOSE = False
steps = 0

def shorfactor(n, p_alg, seed=None):
    random.seed(seed)
    keepgoing = True
    guess1 = None
    guess2 = None
    global steps
    g = 2
    while(keepgoing):
        steps += 1
        g += 1#random.randint(2,n-1)
        if VERBOSE: print("g is ",g)
        common_den = np.gcd(g,n)
        if(common_den!=1):
            if VERBOSE: print("g shares a factor with n, breaking out")
            result = common_den, n//common_den
            guessG(n, result[1])
            return result
        p = p_alg(n,g)
        guess1 = g**(p//2) + 1
        if VERBOSE: print(guess1)
        guess2 = g**(p//2) - 1
        #print(guess2)
        if(p%2==1):
            continue
        if (guess1%n == 0 ):
            continue
        if(guess2%n == 0 ):
            continue
        keepgoing = False
    factor1 = np.gcd(guess1,n)
    result = (factor1, n//factor1)
    guessG(n, result[1])
    return (factor1, n//factor1)

def findp(n,g):
    for i in range(1,n):
        global steps
        steps += 1
        raisedpow = g**i
        remainder = raisedpow % n
        if (remainder ==1):
            return i

def guessG(N,g):
    if g != 1:
        if N != g:
            if N % g == 0:
                a = g
                b = N/g
                print("FOUND a = "+str(a)+", b = "+str(b))
                return True
    return False

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
    if VERBOSE: print("shadowing quantum")
    powerpos = generaterangeSuperPosition(n)
    raisedpows = superpositionPow(g,powerpos,modulo=n)
    if VERBOSE: print("raised pows",raisedpows)
    collapse = raisedpows.collapseTupleSuperPosition()
    if VERBOSE: print("collapsed raised pows",collapse)
    p = cheatingFourierTransform(collapse, n)
    if VERBOSE: print("quantum p found to be",p)
    return p

def cheatingFourierTransform(sup,n):
    return (sup.values[1][0] - sup.values[0][0]) % n

def bruteFactor(N):
    g = 2
    global steps
    while not guessG(N,g):
        steps += 1
        g+=1


def timeAlg(alg, N, p_func = None):
    print("Running " + alg.__name__)
    time1 = time.time()
    if p_func == None:
        alg(N)
    else:
        print("With " + p_func.__name__)
        alg(N, p_func)
    time2 = time.time()
    print("Time was: " + str(time2 - time1))
    global steps
    print("Steps were: ", steps)
    steps = 0
    print("")

def main():
    N = util.getN(7)
    print("")
    timeAlg(bruteFactor, N)
    timeAlg(shorfactor, N, findp)
    timeAlg(shorfactor, N, findpQuantum)


if __name__ == "__main__":
    main()

# print(shorfactor(55))
# a = superPosition([55,44])
# print(a.collapseSuperposition())
