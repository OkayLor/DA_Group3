import unittest
from scrapytest import NewSpider

class TestNewSpider(unittest.TestCase):
    def test_start_urls(self):
        spider = NewSpider()
        expected_url = 'http://172.18.58.80/creative'
        actual_url = spider.start_urls[0]
        self.assertEqual(actual_url, expected_url)