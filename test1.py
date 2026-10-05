import unittest

from prime import is_prime

class Tests(unittest.TestCase):

    def test_1(self):
        """Checks 1 is not a prime number."""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """Checks 2 is a prime number."""
        self.assertTrue(is_prime(2))

    def test_8(self):
        """Checks 8 is not a prime number."""
        self.assertFalse(is_prime(8))

    def test_11(self):
        """Checks 1 is a prime number."""
        self.assertTrue(is_prime(11))

    def test_25(self):
        """Checks 25 is not a prime number."""
        self.assertFalse(is_prime(25))

    def test_28(self):
        """Checks 28 is not a prime number."""
        self.assertFalse(is_prime(28))

if __name__ == "__main__":
    unittest.main()