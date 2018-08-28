from calculator import Count
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        print("start")

    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(), 5, msg="ok")

    def test_add2(self):
        j = Count(4, 5)
        self.assertEqual(j.add(), 1, msg="ok1")

    def tearDown(self):
        print("end")

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add2"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
