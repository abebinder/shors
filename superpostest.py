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

    def testgenerateSuperPosIncreasing(self):
       assert shors.generaterangeSuperPosition(5).values == [1,2,3,4,5]

    def testCollapseTupleSuper(self):
        powers = shors.generaterangeSuperPosition(40)
        a = 2
        n = 9
        superposraisedpow = shors.superpositionPow(a, powers,modulo=9)
        collapse = superposraisedpow.collapseTupleSuperPosition()
        print(collapse)

        #in this case p is 6
        assert collapse.values[1][0] - collapse.values[0][0]==6
        assert collapse.values[2][0] - collapse.values[1][0]==6

        #all remainders should be the same. doesn't matter what they are. Onl fact that matters
        # is they are the same and spaced p apart, in this case 6
        assert collapse.values[0][1] == collapse.values[1][1] == collapse.values[2][1]





if __name__ == '__main__':
    unittest.main()