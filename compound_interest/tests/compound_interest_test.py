import unittest
from src.compound_interest import CompoundInterest


class CompoundInterestTest(unittest.TestCase):
    def setUp (self):
        self.case1 = CompoundInterest(100, 0.1, 20, 0)
        self.case2 = CompoundInterest(100, 0.06, 10, 0)
        self.case3 = CompoundInterest(100000, 0.05, 8, 0)
        self.case4 = CompoundInterest(0, 0.1, 1, 0)
        self.case5 = CompoundInterest(100, 0, 10, 0)

        self.case6 = CompoundInterest(100, 0.05, 8, 1000)
        self.case7 = CompoundInterest(100, 0.05, 10, 1000)
        self.case8 = CompoundInterest(116028.86, 0.075, 8, 2006)
        self.case9 = CompoundInterest(116028.86, 0.09, 12, 1456)
        
        

    def test_calculate_case1(self):
        self.assertEqual(732.81, self.case1.calculate())

    def test_calculate_case2(self):
        self.assertEqual(181.94, self.case2.calculate())

    def test_calculate_case3(self):
        self.assertEqual(149058.55, self.case3.calculate())

    def test_calculate_case4(self):
        self.assertEqual(0.00, self.case4.calculate())

    def test_calculate_case5(self):
        self.assertEqual(100.00, self.case5.calculate())

    # def test_calculate_case6(self):
    #     self.assertEqual(118380.16, self.case6.calculate_with_monthly_payment())

    # def test_calculate_case7(self):
    #     self.assertEqual(156093.99, self.case7.calculate_with_monthly_payment())

    # def test_calculate_case8(self):
    #     self.assertEqual(475442.59, self.case8.calculate_with_monthly_payment())

    # def test_calculate_case9(self):
    #     self.assertEqual(718335.96, self.case9.calculate_with_monthly_payment())

    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

