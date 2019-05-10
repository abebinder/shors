# print(shorfactor(55))
# a = superPosition([55,44])

import shors
import unittest

class TestShor(unittest.TestCase):

    def testshorsworksimperitive(self):
        factors = shors.shorfactor(55,1)
        print(factors)
        assert 5 in factors  and 11 in factors

    def testShoresManySeeds(self):
        for i in range(100):
            factors = shors.shorfactor(55,seed=i)
            print(factors)
            assert 5 in factors and 11 in factors

if __name__ == '__main__':
    unittest.main()