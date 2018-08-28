# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")

    def test10(self):
        print("10")

    def test13(self):
        print("13")

    def test12(self):
        print("12")

if __name__ == '__main__':
    unittest.main()