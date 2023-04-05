import unittest
class mytest(unittest.TestCase):
    def test1(self):
        self.assertEqual(1,1)
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')
if __name__ == '__main__':
    unittest.main()