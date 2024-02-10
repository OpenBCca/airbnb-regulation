import json
import scrapy
from scrapy.http import Response


class ListingSpider(scrapy.Spider):
    name = "listing_spider"
    allowed_domains = ['airbnb.ca']
    start_urls = ['https://www.airbnb.ca/s/Vancouver--British-Columbia--Canada/homes']
    next_page_cursors: [str] = None

    def parse(self, response: Response, **kwargs):
        script_tag = response.css('script#data-deferred-state')
        script_inner_text = script_tag.css('script::text').get()
        script_tag_json = json.loads(script_inner_text)
        results = script_tag_json["niobeMinimalClientData"][0][1]["data"]["presentation"]["staysSearch"]["results"] \
            ["searchResults"]
        if ListingSpider.next_page_cursors is None:
            ListingSpider.next_page_cursors = \
                script_tag_json["niobeMinimalClientData"][0][1]["data"]["presentation"]["staysSearch"] \
                    ["results"]["paginationInfo"]["pageCursors"]
        for result in results:
            yield {
                "airbnb_id": result["listing"]["id"],
                "title": result["listing"]["title"],
                "name": result["listing"]["name"]
            }
        print("cursors", ListingSpider.next_page_cursors)

        if len(ListingSpider.next_page_cursors) != 0:
            cursor_id = ListingSpider.next_page_cursors.pop()
            print("cursors after popping", ListingSpider.next_page_cursors)
            next_url = f'https://www.airbnb.ca/s/Vancouver--British-Columbia--Canada/homes?cursor={cursor_id}'
            yield response.follow(next_url, callback=self.parse)
