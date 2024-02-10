import json
import scrapy
from scrapy.http import Response


class ListingSpider(scrapy.Spider):
    name = "listing_spider"
    allowed_domains = ['https://www.airbnb.ca/']
    start_urls = ['https://www.airbnb.ca/s/Vancouver--British-Columbia--Canada/homes']

    def parse(self, response: Response):
        script_tag = response.css('script#data-deferred-state')
        script_inner_text = script_tag.css('script::text').get()
        script_tag_json = json.loads(script_inner_text)
        results = script_tag_json["niobeMinimalClientData"][0][1]["data"]["presentation"]["staysSearch"]["results"] \
            ["searchResults"]
        for result in results:
            yield {
                "airbnb_id": result["listing"]["id"]
            }
