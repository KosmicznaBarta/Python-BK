import unittest
from polys import *

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [2, 1]      # W(x) = 2 + x
        self.p2 = [2, 1, 0]   # jw  (niejednoznaczność)
        self.p3 = [-3, 0, 1]  # W(x) = -3 + x^2
        self.p4 = [3]         # W(x) = 3
        self.p5 = [0]         # zero
        self.p6 = [0, 0, 0]   # zero (niejednoznaczność)
        self.p7 = [0, 1]      # W(x) = x
        self.p8 = [0, 0, 1]   # W(x) = x^2
        print("\nSetUp")

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p3), [-1, 1, 1])
        self.assertEqual(add_poly(self.p7, self.p8), [0, 1, 1]) 

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p3, self.p1), [-5, -1, 1])
        self.assertEqual(sub_poly(self.p8, self.p7), [0, -1, 1])

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p3), [-6, -3, 2, 1])
        self.assertEqual(mul_poly(self.p1, self.p8), [0, 0, 2, 1])

    def test_is_zero(self):
        self.assertTrue(is_zero(self.p5))
        self.assertTrue(is_zero(self.p6))
        self.assertFalse(is_zero(self.p1))
        self.assertFalse(is_zero(self.p8))

    def test_eq_poly(self):
        self.assertTrue(eq_poly(self.p1, self.p2))
        self.assertTrue(eq_poly(self.p5, self.p6))
        self.assertFalse(eq_poly(self.p3, self.p4))
        self.assertFalse(eq_poly(self.p7, self.p8))

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1, 2), 4)
        self.assertEqual(eval_poly(self.p3, 3), 6)

    def test_combine_poly(self):
        self.assertEqual(combine_poly(self.p1, self.p3), [-1, 0, 1])
        self.assertEqual(combine_poly(self.p7, self.p8), [0, 0, 1])

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p1, 2), [4, 4, 1])
        self.assertEqual(pow_poly(self.p7, 3), [0, 0, 0, 1])

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p3), [0, 2])
        self.assertEqual(diff_poly(self.p8), [0, 2])

    def tearDown(self):
        print("TearDown")

if __name__ == '__main__':
    unittest.main()