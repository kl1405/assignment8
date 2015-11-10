import unittest
from unittest import TestCase
from investment import *

# author: kaiwen Liu

""" this is a test for assignment8 """

class test(unittest.TestCase):

    def setUp(self):
        pass

    def test_totalvalue(self):
    	a = invest(1000, 10000)
        self.assertEqual(a.positions, 1000)
        b = invest(1, 10000)
        self.assertEqual(b.positions * 1000, 1000)
        c = invest(10, 10000)
        self.assertEqual(c.positions * 100, 1000)
        d = invest(100, 10000)
        self.assertEqual(d.positions * 10, 1000)

if __name__ == '__main__':
    unittest.main()