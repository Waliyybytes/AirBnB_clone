#!usr/bin/env python3
"""
Performed test on console using a  python module
"""

import unittest
import console


class TestConsole(unittest.TestCase):
    """
    Unit Test for the console module
    """

    def setup(self):
        pass

    def test_quit(self):
        """Test the quit command"""
        x = console.quit()
        self.assertTrue(x)
        


if __name__ == "__main__":
    unittest.main()
