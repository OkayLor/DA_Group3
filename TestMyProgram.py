import unittest

class TestMyProgram(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('http://172.18.58.80/creative'.upper(), 'http://172.18.58.80/creative')

    def test_isupper(self):
        self.assertTrue('http://172.18.58.80/creative'.isupper())
        self.assertFalse('http://172.18.58.80/Creative'.isupper())

if __name__ == '__main__':
    unittest.main()