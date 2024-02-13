import json
from typing import Any
import scrapy
from scrapy import Request, Selector
from scrapy.http import Response
from airbnb_listings.items import AirBnBListingItem
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ListingSpider(scrapy.Spider):
    name = "listing_spider"
    allowed_domains = ['airbnb.ca']
    start_urls = ['https://www.airbnb.ca/s/Vancouver--British-Columbia--Canada/homes']
    next_page_cursors: [str] = None

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.driver = webdriver.Chrome()
    #     chrome_options = Options()
    #     chrome_options.add_argument('--headless')
    #     chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    #     self.driver = webdriver.Chrome(options=chrome_options)
    #     self.print = True

    async def parse(self, response: Response, **kwargs):
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
            listing_id = result["listing"]["id"]
            page_url = f"https://www.airbnb.ca/rooms/{listing_id}"
            airbnb_params = {"airbnb_listing_id": listing_id, "title": result["listing"]["title"],
                             "name": result["listing"]["name"]}
            registration_id = "Not Found"
            try:
                print("before registration")
                registration = yield Request(url=page_url, callback=self.handle_listing,
                                             meta={'airbnb_params': airbnb_params})

            except Exception as e:
                print("exception", e)

        if len(ListingSpider.next_page_cursors) != 0:
            cursor_id = ListingSpider.next_page_cursors.pop()
            print("cursors after popping", ListingSpider.next_page_cursors)
            next_url = f'https://www.airbnb.ca/s/Vancouver--British-Columbia--Canada/homes?cursor={cursor_id}'
            yield response.follow(next_url, callback=self.parse)

    def handle_listing(self, response):
        airbnb_params = response.meta.get('airbnb_params')
        listing_item = AirBnBListingItem()
        listing_item["airbnb_listing_id"] = airbnb_params.get('airbnb_listing_id')
        listing_item["title"] = airbnb_params.get('title')
        listing_item["name"] = airbnb_params.get('name')
        script_tag = response.css('script#data-deferred-state')
        script_inner_text = script_tag.css('script::text').get()
        script_tag_json = json.loads(script_inner_text)
        registration_number = None
        try:
            sections = \
                script_tag_json["niobeMinimalClientData"][0][1]["data"]["presentation"]["stayProductDetailPage"][
                    "sections"]["sections"]
            for section in sections:
                if section["sectionComponentType"] == "HOST_PROFILE_DEFAULT":
                    items = section["section"]["hostFeatures"]
                    for item in items:
                        if item["title"] == "Registration number":
                            registration_number = item["subtitle"]
        except Exception as e:
            print("exception", e.args[0])
            registration_number = "Not Found"
        if registration_number is None:
            registration_number = "Not found"
        listing_item["registration_id"] = registration_number
        yield listing_item
