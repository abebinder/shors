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
        assert(superposraisedpow.values==[(1, 5), (2, 4), (3, 6), (4, 2)])

if __name__ == '__main__':
    unittest.main()