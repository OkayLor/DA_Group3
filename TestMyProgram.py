import unittest

class TestMyProgram(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('HTTP://172.18.58.80/CREATIVE'.upper(), 'http://172.18.58.80/creative')

    def test_isupper(self):
        self.assertTrue('http://172.18.58.80/creative'.isupper())
        self.assertFalse('HTTP://172.18.58.80/CREATIVE'.isupper())

if __name__ == '__main__':
    unittest.main()