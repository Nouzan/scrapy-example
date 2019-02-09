import scrapy
from scrapy.selector import Selector
from ..items import DataItem


class BitmexSpider(scrapy.Spider):
    name = "bitmex"
    start_urls = [
        'https://s3-eu-west-1.amazonaws.com/public.bitmex.com/?delimiter=/&prefix=data/trade/'
    ]

    def parse(self, response):
        sel = Selector(text=response.body)
        urls = sel.xpath('//contents/key/text()').getall()
        HOST = 'https://s3-eu-west-1.amazonaws.com/public.bitmex.com/'

        for url in urls:
            link = HOST + url
            data = DataItem()
            data['file_urls'] = [link]
            yield data

