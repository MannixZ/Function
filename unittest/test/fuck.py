from count import is_prime
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        print("start")

    def test_case(self):
        self.assertTrue(is_prime(6), msg= 'hahahaha')

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestCount("test_case"))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)