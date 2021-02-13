import unittest

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], ".."))

from fizzbuzz import fizzbuzz


class TestFizzBuss(unittest.TestCase):

    def test_divisible_by_three(self):
        self.assertEqual("Fizz", fizzbuzz(9))

    def test_divisible_by_five(self):
        self.assertEqual("Buzz", fizzbuzz(20))

    def test_divisible_by_three_and_five(self):
        self.assertEqual("FizzBuzz", fizzbuzz(15))

    def test_divisible_by_neither(self):
        self.assertEqual(7, fizzbuzz(7))


if __name__ == "__main__":
    unittest.main()
