import project.fizzbuzz as fizzbuzz
import unittest


class TestFizzBuss(unittest.TestCase):

    def test_divisible_by_three(self):
        self.assertEqual("Fizz", fizzbuzz.fizzbuzz(9))

    def test_divisible_by_five(self):
        self.assertEqual("Buzz", fizzbuzz.fizzbuzz(20))

    def test_divisible_by_three_and_five(self):
        self.assertEqual("FizzBuzz", fizzbuzz.fizzbuzz(15))

    def test_divisible_by_neither(self):
        self.assertEqual(7, fizzbuzz.fizzbuzz(7))


if __name__ == "__main__":
    unittest.main()
