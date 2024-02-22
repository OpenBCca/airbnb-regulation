# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class AirbnbListingsPipeline:
    def process_item(self, item, spider):
        return item


class AirBnbListingsDuplicatePipeLine:
    """Pipeline for handling duplicate Airbnb listings."""

    @classmethod
    def from_crawler(cls, crawler):
        """
        Create a new instance of the spider from a Scrapy crawler.
        This method sets the file name for which the pipeline should check for duplicates.

       Args:
           crawler: The Scrapy crawler object.

       Returns:
            An instance of the spider.
        """
        csv_file_name = crawler.settings.get("CSV_STORE_FILE_NAME")
        return cls(csv_file_name)

    def __init__(self, csv_file_name):
        """Initialize the pipeline with an empty set of scraped Airbnb IDs."""
        self.airbnb_ids_scrapped = set()
        self.csv_file_name = csv_file_name

    def open_spider(self, spider):
        """
        Open the spider and load existing IDs from the CSV file if it exists.

        If the file does not exist, initialize an empty set.

        Args:
            spider (Spider): The Scrapy spider instance.
        """
        try:
            with open(
                    f"{self.csv_file_name}",
                    "r",
                    encoding="utf8") as file:
                read_csv_file = csv.DictReader(file)
                for row in read_csv_file:
                    row: dict
                    self.airbnb_ids_scrapped.add(row['airbnb_listing_id'])
        except FileNotFoundError as e:
            print(e)

    def process_item(self, item, spider):
        """
        Process each item and check for duplicates.

        If a duplicate Airbnb ID is found, drop the item. Otherwise, add the ID to the set and return the item.

        Args:
            item (Item): The Scrapy item being processed.
            spider (Spider): The Scrapy spider instance.

        Returns:
            Item: The processed item, or None if the item was dropped.
        """
        adapter = ItemAdapter(item)
        if adapter["airbnb_listing_id"] in self.airbnb_ids_scrapped:
            raise DropItem(f"Duplicate airbnb id found: {item!r}")
        else:
            self.airbnb_ids_scrapped.add(adapter["airbnb_listing_id"])
            return item


class AirbnbListingsPipelineDataCleaner:
    """
    A pipeline for cleaning Airbnb listing data.

    Attributes:
    - fields_to_lower_case (list): A list of field names to convert to lowercase.
    """

    fields_to_lower_case = ["title", "name"]

    def process_item(self, item, spider):
        """
        Process an item from the spider.
        Checks to see if registration number is empty.
        Makes the name and title field lowercase.

        Args:
        - item (dict): The item to process.
        - spider: The spider that crawled the item.

        Returns:
        - dict: The processed item.
        """
        adapter = ItemAdapter(item)

        # name and title fields are lowercase
        for key in AirbnbListingsPipelineDataCleaner.fields_to_lower_case:
            value: str = adapter.get(key)
            value = value.lower()
            adapter[key] = value

        # checks if registration number is empty
        registration_number: str = adapter.get('registration_number')
        if not registration_number.strip():
            registration_number = "Not Found"
            adapter['registration_number'] = registration_number

        return item
