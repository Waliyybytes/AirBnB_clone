#!usr/bin/env python3
"""
Performed test on console using a  python module
"""

import os
import sys
import unittest
from console import Console
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """
    Unit Test for the console module
    """

    def setup(self):
        pass

    @patch('console.do_quit')
    def test_quit(self,mock_do_quit):
        """Test the quit command"""
        mock_do_quit.return_value = True
        assertEqual(do_quit(),True)
        


if __name__ == "__main__":
    unittest.main()
