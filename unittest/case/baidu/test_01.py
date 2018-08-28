# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start")

    @classmethod
    def tearDownClass(cls):
        print("end")

    def test01(self):
        u'判断 a == b'
        a = 1
        b = 1
        self.assertEqual(a, b)

    def test03(self):
        u'判断 a in b'
        a = 'hello'
        b = 'hello,asdas'
        self.assertIn(a, b)

    def test02(self):
        u'判断 a is True'
        a = True
        self.assertTrue(a)

    def test04(self):
        "失败东西"
        a = 1
        b = 3
        self.assertEqual(a, b,msg="%s 不能等于 %s" %(a, b))

if __name__ == '__main__':
    unittest.main()
