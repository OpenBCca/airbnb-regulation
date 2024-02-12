# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AirbnbListingsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AirBnBListingItem(scrapy.Item):
    airbnb_listing_id = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    registration_id = scrapy.Field()
