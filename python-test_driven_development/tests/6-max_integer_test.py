#!/usr/bin/python3
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test case for the max_integer function."""

    def test_positive_integers(self):
        """Test with a list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test with a mix of positive and negative integers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_all_same(self):
        """Test with a list where all elements are the same."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_values(self):
        """Test with a list containing float values."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_integers_and_floats(self):
        """Test with a list containing both integers and floats."""
        self.assertEqual(max_integer([1.1, 2, 3.3, 4]), 4)

    def test_string_list(self):
        """Test with a list of strings (valid comparison based on lexicographical order)."""
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')

    def test_single_string(self):
        """Test with a single string (each character is treated as an element in the list)."""
        self.assertEqual(max_integer('abcd'), 'd')

    def test_none_input(self):
        """Test with None as input (should raise a TypeError)."""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
