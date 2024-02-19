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

    file_name = "master_data.csv"

    def __init__(self):
        """Initialize the pipeline with an empty set of scraped Airbnb IDs."""
        self.airbnb_ids_scrapped = set()

    def open_spider(self, spider):
        """
        Open the spider and load existing IDs from the CSV file if it exists.

        If the file does not exist, initialize an empty set.

        Args:
            spider (Spider): The Scrapy spider instance.
        """
        try:
            with open(
                    f"D:\OneDrive - BCIT\openBC\\airbnb\\airbnb-regulation\ingestion\\airbnb_scrapping\{AirBnbListingsDuplicatePipeLine.file_name}",
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
