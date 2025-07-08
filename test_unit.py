import unittest

class Test:
    def factorial(self,chis):
        if chis == 0:
            return 1
        else:
            return chis * self.factorial(chis-1)


    def stepan(self,chis , step):
        return chis ** step


    def formula(self,a,b):
        return (a ** 2) + (b ** 2)

test = Test()

class Unit_test(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(test.factorial(5),720)
    def test_stepan(self):
        self.assertEqual(test.stepan(6,2),36)
    def test_fact(self):
        self.assertEqual(test.formula(2,3),13)

unittest.main()
