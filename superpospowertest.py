import shors
import unittest

class TestStringMethods(unittest.TestCase):

    def testSuperPosRaisePow(self):
        powers = shors.superPosition([1,2,3,4])
        a = 5
        superposraisedpow = shors.superpositionPow(a,powers)
        assert superposraisedpow.values == [(1,5),(2,25),(3,125),(4,625)]

    def testSuperPosRaisePowModulo(self):
        powers = shors.superPosition([1,2,3,4])
        a = 5
        superposraisedpow = shors.superpositionPow(a,powers,modulo=7)
        print(superposraisedpow)

if __name__ == '__main__':
    unittest.main()