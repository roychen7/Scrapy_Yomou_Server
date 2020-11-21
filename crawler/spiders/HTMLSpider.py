import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import pymongo

class HTMLSpider(scrapy.Spider):
    name = 'HTMLSpider'

    # overwrite default constructor to account for arguments (etc url)
    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.unique_id = kwargs.get('unique_id')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        HTMLSpider.rules = [
           Rule(LinkExtractor(unique=True), callback='parse'),
        ]
        super(HTMLSpider, self).__init__(*args, **kwargs)

    # return dict containing HTML of scrapy response
    def parse(self, response):
        i = {}
        i['res'] = response.body.decode('utf-8')
        return i