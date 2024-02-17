# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AirBnBListingItem(scrapy.Item):
    """
    Item class representing an Airbnb listing.

    Attributes:
        airbnb_listing_id (str): The Airbnb listing ID.
        title (str): The title of the listing.
        name (str): The name of the listing.
        registration_number (str): The registration number of the listing.
        latitude (float): The latitude coordinate of the listing.
        longitude (float): The longitude coordinate of the listing.
    """
    airbnb_listing_id = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    registration_number = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
