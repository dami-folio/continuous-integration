# this file will be used for unit testing.

import unittest
from test_function import inverter

class perform_unit_tests(unittest.TestCase):
    def test_add(self):

        # testing typical input
        self.assertEqual(inverter(7), -7)

        # more typical input
        self.assertEqual(inverter(-14.3), 14.3)

        # testing string input
        self.assertEqual(inverter("hi"), "invalid input")

        # testing mixed input
        self.assertEqual(inverter("12 apples"), "invalid input")

# call unit test function 

if __name__ == "__main__":
    unittest.main()