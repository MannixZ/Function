# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")

    def test07(self):
        print("07")

    def test09(self):
        print("09")

    def test08(self):
        print("08")

if __name__ == '__main__':
    unittest.main()