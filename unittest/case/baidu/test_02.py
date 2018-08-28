# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")

    def test04(self):
        print("04")

    def test06(self):
        print("06")

    def test05(self):
        print("05")

if __name__ == '__main__':
    unittest.main()