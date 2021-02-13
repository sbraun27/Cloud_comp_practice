import black_scholes
import unittest
import numpy


class BSTestCases(unittest.TestCase):

    def test_call(self):
        self.assertAlmostEqual(
            0.0000, black_scholes.european_option(S=1, K=1000, r=0., T=30, sigma=0.01, type="c"))

    def test_put(self):
        self.assertAlmostEqual(
            0.0000, black_scholes.european_option(S=1000, K=1, r=0, T=30, sigma=0.01, type="p"))

    def test_no_type(self):
        self.assertEqual(None, black_scholes.european_option(
            S=1000, K=1, r=0, T=30, sigma=0.01, type="yolo"))

    def test_negative_S(self):
        self.assertEqual(None, black_scholes.european_option(
            S=-100, K=100, r=0.01, T=100, sigma=0.01))

    def test_negative_K(self):
        self.assertEqual(None, black_scholes.european_option(
            S=100, K=-100, r=0.01, T=100, sigma=0.01))

    def test_call_price(self):
        self.assertEqual(25.9182, black_scholes.european_option(
            S=100, K=100, r=0.01, T=30, sigma=0.01, type="c"))

    def test_put_price(self):
        self.assertEqual(11.1824, black_scholes.european_option(
            S=100, K=150, r=0.01, T=30, sigma=0.01, type="p"))


if __name__ == "__main__":
    unittest.main()
