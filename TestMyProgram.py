import unittest
import Browser

class TestMyProgram(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('http://172.18.58.80/creative'.upper(), 'HTTP://172.18.58.80/CREATIVE')

    def test_isupper(self):
        self.assertTrue('HTTP://172.18.58.80/CREATIVE'.isupper())
        self.assertFalse('http://172.18.58.80/creative'.isupper())


    def test_my_program(self):
        result = my_program('http://172.18.58.80/creative', 'HTTP://172.18.58.80/CREATIVE') # Call your program function here
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()