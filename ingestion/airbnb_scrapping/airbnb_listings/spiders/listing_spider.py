import scrapy
from scrapy.http import Response


class ListingSpider(scrapy.Spider):
    name = "listing_spider"
    allowed_domains = ['https://www.airbnb.ca/']
    start_urls = ['https://www.airbnb.ca/s/Vancouver--British-Columbia--Canada/homes']

    def parse(self, response: Response):
        pass


