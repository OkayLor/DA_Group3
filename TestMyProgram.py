import unittest
from scrapytest import NewSpider
import requests

# To check if the url in scrapytest.py is the correct url
class TestNewSpider(unittest.TestCase):
    def test_start_urls(self):
        spider = NewSpider()
        expected_url = 'http://172.18.58.80/creative'
        actual_url = spider.start_urls[0]
        self.assertEqual(actual_url, expected_url)


url = "http://172.18.58.80/creative"

class TestMyProgram(unittest.TestCase):


    # Checking whether the url is responding to requests
    def test_TestUrl(self):
        try:
            resp = requests.get(url)
            if int(resp.status_code) == 200:
                print("[TestUrl] URL OK")
            else:
                print("[TestUrl] Requested URL not found")
        except Exception as e:
            print("[TestUrl] Error: ", {e})

if __name__ == '__main__':
    unittest.main()