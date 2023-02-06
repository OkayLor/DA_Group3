import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://bricksetcom/sets/year-2019']